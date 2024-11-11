from logger import logger
from reader import get_data
from writer import create_yml

logger.info('START')
try:
    header, body = get_data()
    create_yml(header, body)
except Exception as e:
    logger.critical(e, exc_info=True)
    logger.error('something went wrong')

logger.info('END\n\n')

