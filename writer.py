import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
import copy
import os
from logger import  logger
from classes import *
from manage import project_root

"""
header = CatalogData() obj with categories
body: list of dicts of offers for every catalogue
scope: list with settings 
"""

def create_yml(header, body):
    yml_name = 'doctors.xml'

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    # create header
    data = ET.Element('yml_catalog')
    data.set('date', dt_string)
    shop = ET.SubElement(data, 'shop')
    name = ET.SubElement(shop, 'name')
    name.text = header.name
    company = ET.SubElement(shop, 'company')
    company.text = header.company
    url = ET.SubElement(shop, 'url')
    url.text = header.url
    picture = ET.SubElement(shop, 'picture')
    picture.text = header.picture
    currencies = ET.SubElement(shop, 'currencies')
    currency = currencies.makeelement('currency', header.currency)
    currencies.append(currency)
    categories = ET.SubElement(shop, 'categories')
    for cat in header.categories:
        category = ET.SubElement(categories, 'category')
        category.set('id', cat['id'])
        category.text = cat['content']
    sets = ET.SubElement(shop, 'sets')
    for item in header.sets:
        set = ET.SubElement(categories, 'set')
        set.set('id', item['id'])
        name = ET.SubElement(set, 'name')
        name.text = item['name']
        url = ET.SubElement(set, 'url')
        url.text = item['url']
    # create body
    offers = ET.SubElement(shop, 'offers')

    for item in body:
        profession = [d["id"] for d in header.sets if d["id"] in item.profession]
        if item.experience_years and len(profession) > 0:
            try:
                offer = ET.SubElement(offers, 'offer')
                offer.set('id', item.id)
                url = ET.SubElement(offer, 'url')
                url.text = item.url
                price = ET.SubElement(offer, 'price')
                price.text = item.price

                currencyId = ET.SubElement(offer, 'currencyId')
                currencyId.text = item.currencyId
                categoryId = ET.SubElement(offer, 'categoryId')
                categoryId.text = item.categoryId
                set_ids = ET.SubElement(offer, 'set_ids')

                print(profession, item.profession)
                set_ids.text = ",".join(profession)
                picture = ET.SubElement(offer, 'picture')
                picture.text = item.avatar
                name = ET.SubElement(offer, 'name')
                name.text = item.full_name
                # description = ET.SubElement(offer, 'description')
                # description.text = item.description
                params = item.get_params()

                for key in params.keys():
                    if params[key] != '' and params[key] != 'none':
                        param = ET.SubElement(offer, 'param')
                        param.set('name', key)
                        param.text = params[key]
                    else:
                        logger.error(f'{key} raised in error. param skippet in item {item.id}')
            except:
                logger.error('%s raised an error' % item.name)
                raise
        else:
            logger.error(f'item {item.id} has lack of data provided. item is skipped')
    mydata = minidom.parseString(ET.tostring(data)).toprettyxml(indent='    ')

    # os.mkdir('yml')
    print(f'{project_root}/yml/{yml_name}')
    with open(f'{project_root}/yml/{yml_name}', 'w', encoding='utf-8') as yml:
        yml.write(mydata)

