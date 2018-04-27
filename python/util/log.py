import os, sys
import logging

LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'log')
LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'log', 'RCScv.log')

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)
if not os.path.isfile(LOG_PATH):
    f = open(LOG_PATH, 'w+')

formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)-s]: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.FileHandler(LOG_PATH)
handler.setFormatter(formatter)

logger = logging.getLogger('RCScv')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.info('Logging setup for %s' % LOG_PATH)