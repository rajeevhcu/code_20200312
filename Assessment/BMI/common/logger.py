import logging
from datetime import datetime
import os

if not os.path.exists('./logger'):
    os.mkdir('./logger')
file_path = './logger/app_{}.log'.format(datetime.now().strftime('%d_%m_%Y'))
logging.basicConfig(filename=file_path,
                    format='[%(levelname)s] - [%(asctime)s] - [%(name)s - %(lineno)s] - %(message)s',
                    level=logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

# set a format which is simpler for console use
formatter = logging.Formatter('[%(levelname)s] - [%(asctime)s] - [%(name)s - %(lineno)s] - %(message)s')
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)


def get_logger(name):
    return logging.getLogger(name)
