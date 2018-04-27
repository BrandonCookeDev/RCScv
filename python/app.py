import os, sys
import logging
from util import log
from util.config import Config as Config
from lib.RCScv import RCScv as RCScv
from lib import stock_cropper
from lib import letterbox_cropper

config = Config()

logger = logging.getLogger('RCScv')
logger.info('RCScv: Beginning Main')

ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, '..', 'resources')
MELEE1 = os.path.join(RESOURCES_DIR, 'Melee1.png')
MELEE2 = os.path.join(RESOURCES_DIR, 'Melee2.png')
MELEE3 = os.path.join(RESOURCES_DIR, 'Melee3.jpg')
MELEE4 = os.path.join(RESOURCES_DIR, 'Melee4.jpg')
LETTERBOXED = os.path.join(RESOURCES_DIR, 'LetterboxedMelee.png')
CROPPED_LETTERBOX = os.path.join(RESOURCES_DIR, 'UnletterboxedMelee.png')

if __name__ == '__main__':
    framecv = RCScv(LETTERBOXED, CROPPED_LETTERBOX)
    if framecv.cvimage.shape[0] > 480:
        new_frame_cv = letterbox_cropper.crop_letterbox(LETTERBOXED)
        new_frame_cv.save(CROPPED_LETTERBOX)
        stock_cropper.process_frame(CROPPED_LETTERBOX)
    else:
        stock_cropper.process_frame(LETTERBOXED)
    
