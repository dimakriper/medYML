import requests
import classes
from logger import logger
from manage import api_key

def get_data():
    doctors = []
    clinic = classes.Shop()

    clinic.get_content()


    d = requests.post('https://app.rnova.org/api/public/getUsers', {'api_key': api_key})
    doctors_list = d.json()['data']

    for item in doctors_list:
        try:
            # print(item)
            doctor = classes.Offer()
            doctor.set_content(item)
            # print(doctor)
            doctor.set_price()
            doctors.append(doctor)
        except Exception as e:
            logger.critical(e, exc_info=True)
            logger.error('following item is skipped %s' % (item))

    return [clinic, doctors]
