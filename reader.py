import requests
import classes
from logger import logger
from manage import api_key

def get_data():
    keep_list = {'surnames':
            [
                'Антропова',
                'Петерсен',
                'Коротаев',
                'Лавникович',
                'Захаренко',
                'Гурьев',
                'Пицына',
                'Капранов',
            ],
        'items': []
                   }
    doctors = []



    d = requests.post('https://app.rnova.org/api/public/getUsers', {'api_key': api_key})
    doctors_list = d.json()['data']

    for item in doctors_list:
        if '451' not in item["profession"] and '764' not in item["profession"]:
            # print(doctor)
            try:
                # print(item)
                doctor = classes.Offer()
                doctor.set_content(item)
                # print(doctor)
                if any(doctor.full_name.startswith(name) for name in keep_list['surnames']):
                    doctor.set_price()
                    doctors.append(doctor)
                    keep_list['items'].append(doctor)
                else:
                    logger.info(f"Doctor {doctor.full_name} starts with an ignored string and will be skipped.")

            except Exception as e:
                logger.critical(e, exc_info=True)
                logger.error('following item is skipped %s' % (item))

    clinic = classes.Shop()

    clinic.get_content(keep_list)

    return [clinic, doctors, keep_list]
