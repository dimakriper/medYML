import re
import requests
import manage

def remove_pattern(input_string, pattern):
    # Используйте re.sub для замены совпадений шаблона пустой строкой
    result = re.sub(pattern, '', input_string)
    return result


class Shop:
    def __init__(self):
        self.name = 'МЕДИКОР'
        self.company = 'ООО "МЕДИКОР"'
        self.url = 'https://mcmedikor.ru'
        self.email = 'support-doctors@doctors.sample.s3.yandex.net'
        self.picture = 'https://mcmedikor.ru/f/logotip_cnm.jpg'
        self.description = 'Каталог врачей'
        self.currency = {'id': 'RUR', 'rate': '1'}
        self.categories = [{'id' : "1", 'content' : "Врач"}]
        self.sets = []

    def get_content(self):
        professions = manage.get_included_professions()
        prof_ids = professions.keys()
        for id in prof_ids:
            self.sets.append({
                'name': professions[id],
                'url': f'https://mcmedikor.ru/zapis-na-vizit?profession={id}',
                'id': str(id)
            })

class Offer:
    def __init__(self):
        self.service_id = ''
        self.id = ''
        self.url = ''
        self.price = '0'
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
        self.shop_name = 'МЕДИКОР'
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
            "Телефон для записи": '+7 (4852) 20-85-03',
            "внутренний идентификатор врача": self.id,
            "внутренний идентификатор клиники": '550',
            "Вызов на дом": self.is_outside,
            "Прием по видеосвязи": self.is_telemedicine,
            "Категория": self.qualification,
            "Онлайн-расписание": 'true',
            # TODO: add education, add schedule
        }
    def set_content(self, data):
        if '1914' in data["role"]:
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
            self.description = data["doctor_info"]
            self.date_work_from = f'{data["date_work_from"]}'.lower()
            self.work_degree = f'{data["work_degree"]}'.lower()
            self.work_rank = f'{data["work_rank"]}'.lower()
            self.work_academy_status =f'{ data["work_academy_status"]}'.lower()
            self.qualification = data["qualification"].split()[0] if data["qualification"] else 'none'
            print(self.qualification)
            self.education = data["education"]
            self.id = f'{data["id"]}'.lower()
            self.url = f'https://mcmedikor.ru/zapis-na-vizit?doctor={self.id}'
            self.education_courses = data['education_courses']


    def set_price(self):
        if self.id:
            p = requests.post('https://app.rnova.org/api/public/getServices',
                              {'api_key': manage.api_key, 'user_id': self.id, 'term': "Консультация"})
            p_data = p.json()["data"]

            if p_data:
                print(p_data[0]['title'])
                self.price = str(p_data[0]['price']) #default 0


