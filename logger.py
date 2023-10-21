import logging
import os


x = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.split(x)[0]

logging.basicConfig(handlers=[logging.FileHandler(filename= project_root + os.sep + 'medYML' + os.sep + 'LOG.log',
                                                 encoding='utf-8'),
                              logging.StreamHandler()],
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s - %(message)s',
                    )

logger = logging.getLogger(__name__)