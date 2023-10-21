import os
from configparser import ConfigParser
import re
from logger import logger
"""
This module is for getting paths to input data (CMLs in folder)
and settings for output files
"""

x = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.split(x)[0] + os.sep + 'medYML'

config = ConfigParser()
config.read(project_root + os.sep + 'settings.ini')

creds = config['CREDS']
api_key = creds['api_key']
# webdata_folder = roots['webdata_root']
# csv_file = project_root + os.sep + 'options.csv'
# pictures_dir = roots['pictures_root']



