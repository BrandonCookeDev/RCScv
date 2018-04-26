import os, sys
import logging
from util import log
from util.config import Config as Config
from lib import RCScv as rcscv
from lib import stock_cropper

config = Config()

logger = logging.getLogger('RCScv')
logger.info('RCScv: Beginning Main')

ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, '..', 'resources')
MELEE1 = os.path.join(RESOURCES_DIR, 'Melee1.png')
MELEE2 = os.path.join(RESOURCES_DIR, 'Melee2.png')
MELEE3 = os.path.join(RESOURCES_DIR, 'Melee3.jpg')
MELEE4 = os.path.join(RESOURCES_DIR, 'Melee4.jpg')

if __name__ == '__main__':
    c = stock_cropper.process_frame(MELEE3)
    
