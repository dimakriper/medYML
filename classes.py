import re
import requests
from manage import api_key

class Shop:
    def __init__(self):
        self.name = 'ЦЕНТР "МЕДИКОР"'
        self.company = 'ООО "МЕДИКОР"'
        self.url = 'https://mcmedikor.ru'
        self.email = 'support-doctors@doctors.sample.s3.yandex.net'
        self.picture = 'https://rawcdn.githack.com/dimakriper/medYML/8a5a17dfdec61c87629819f6a0e6153af2878628/%D0%BB%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF%20%D0%A6%D0%9D%D0%9C.jpg'
        self.description = 'Каталог врачей'
        self.currency = {'id': 'RUR', 'rate': '1'}
        self.categories = [{'id' : "1", 'content' : "Врач"}]
        self.sets = []

    def get_content(self):
        c = requests.post('https://app.rnova.org/api/public/getProfessions',
                          {'api_key': api_key})
        c_data = c.json()["data"]
        for item in c_data:
            if item["doctor_name"] and item["id"] != 451 and item["id"] != 764:
                self.sets.append({
                    'name': item["doctor_name"] if item["doctor_name"] else item["name"],
                    'url': f'https://mcmedikor.ru/zapis-na-vizit?profession={item["id"]}',
                    'id': str(item["id"])
                })

class Offer:
    def __init__(self):
        self.id = ''
        self.url = ''
        self.price = ''
        self.currencyId = 'RUR'
        self.categoryId = '1'
        self.set_ids = []
        self.picture = ''
        self.description = ''
        self.categoryId = "1"
        self.name = ''
        self.surname = ''
        self.midname = ''
        self.experience_years = ''
        self.adult = ''
        self.child = ''
        self.work_degree = ''
        self.work_rank = ''
        self.work_academy_status = ''
        self.education = ''
        self.education_courses = ''
        self.qualification = ''
        self.shop_city = 'г. Ярославль'
        self.shop_address = 'г. Ярославль, ул. Республиканская, д. 16, к. А'
        self.offer_address= ''
        self.shop_name = ''
        self.appointment = 'true'
        self.date_work_from = ''
        self.profession = ''
        self.profession_titles = ''
        self.phone = ''
        self.email = ''
        self.is_outside = ''
        self.is_telemedicine = ''
        self.avatar = ''
        self.has_company = ''
        self.full_name = ''
        self.shop_name = 'ЦЕНТР "МЕДИКОР"'
    def get_params(self):
        return {
            "Фамилия" : self.surname ,
            "Имя": self.name,
            "Отчество": self.midname,
            "Годы опыта": self.experience_years,
            "Город": self.shop_city,
            "Взрослый врач": self.adult,
            "Детский врач": self.child,
            "Город клиники": self.shop_city,
            "Адрес клиники": self.shop_address,
            "Название клиники": self.shop_name,
            "Возможность записи": self.appointment,
            "Телефон для записи": self.phone,
            "внутренний идентификатор врача": self.id,
            "внутренний идентификатор клиники": '550',
            "Вызов на дом": self.is_outside,
            "Прием по видеосвязи": self.is_telemedicine,
            "Категория": self.qualification
            # TODO: add education, add schedule
        }
    def set_content(self, data):
        if data["role"][0] == '1914':
            self.avatar = data["avatar"]
            if len(data["contacts"]) > 0 and data["contacts"][0]["type"] == 'mobile': self.phone = data["contacts"][0]["value"]
            self.surname, self.name, self.midname = data["name"].split()
            self.profession = data["profession"]
            self.profession_titles = data["profession_titles"]
            self.has_company = f'{data["has_company"]}'.lower()
            self.child = f'{data["is_child_doctor"]}'.lower()
            self.adult = f'{data["is_adult_doctor"]}'.lower()
            self.is_outside = f'{data["is_outside"]}'.lower() if data["is_outside"] else 'false'
            self.is_telemedicine = f'{data["is_telemedicine"]}'.lower() if data["is_telemedicine"] else 'false'
            self.full_name = data["name"]
            self.experience_years = data["work_period"].split()[0]

            self.date_work_from = f'{data["date_work_from"]}'.lower()
            self.work_degree = f'{data["work_degree"]}'.lower()
            self.work_rank = f'{data["work_rank"]}'.lower()
            self.work_academy_status =f'{ data["work_academy_status"]}'.lower()
            self.qualification = data["qualification"].split()[0] if data["qualification"] else 'none'
            print(self.qualification)
            self.education = data["education"]
            self.id = f'{data["id"]}'.lower()
            self.url = f'https://mcmedikor.ru/zapis-na-vizit?doctor={self.id}'

    def set_price(self):
        if self.id:
            p = requests.post('https://app.rnova.org/api/public/getServices',
                              {'api_key': api_key, 'user_id': self.id})
            p_data = p.json()["data"]
            for item in p_data:
                if item["title"].find('Доплата') == -1:
                    self.price = item["price"]
                    return

