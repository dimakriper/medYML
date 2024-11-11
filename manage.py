import csv
import os
from configparser import ConfigParser
import re
from logger import logger
"""
This module is for getting paths to input data (CMLs in folder)
and settings for output files
"""
x = os.path.dirname(os.path.abspath(__file__))
project_root = x # os.path.split(x)[0] + os.sep + 'medYML (2)'
print(x, project_root)
config = ConfigParser()
config.read(project_root + os.sep + 'settings.ini')

creds = config['CREDS']
api_key = creds['api_key']

PROFESSIONS_INCLUDED_CSV = project_root + os.sep + 'professions.csv';

def get_included_professions():
    with open(PROFESSIONS_INCLUDED_CSV, newline='', encoding='utf-8') as professions:
        reader = csv.reader(professions, delimiter=':')
        return dict(reader)

# webdata_folder = roots['webdata_root']
# csv_file = project_root + os.sep + 'options.csv'
# pictures_dir = roots['pictures_root']



