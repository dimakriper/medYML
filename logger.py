import logging
import os

x = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.split(x)[0]
log_file_path = os.path.join(project_root, 'medYML', 'LOG.log')

# Clear the log file at the start
with open(log_file_path, 'w'):
    pass

logging.basicConfig(handlers=[logging.FileHandler(filename=log_file_path,
                                                 encoding='utf-8'),
                              logging.StreamHandler()],
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s - %(message)s',
                    )

logger = logging.getLogger(__name__)

# Example usage
logger.info("Logging system initialized.")
