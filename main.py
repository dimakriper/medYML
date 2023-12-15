from logger import logger
from reader import get_data
from writer import create_yml

logger.info('START')
try:
    header, body, keep_list = get_data()
except Exception as e:
    logger.critical(e, exc_info=True)
    logger.error('reader module raised an error')
print(header, body)
create_yml(header, body)
logger.info('END\n\n')

