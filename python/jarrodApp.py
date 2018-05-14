import cv2
import os, sys
import logging
from util import log
from util.config import Config as Config
from lib.RCScv import RCScv as RCScv
from lib.Threader import Threader
from lib.croppers import letterbox_cropper
from lib.detectors import detect_circles
from algorithms import percents as stockDetection

config = Config()
debug_mode = config.get_main_debug_mode()
MELEE_WIDTH = config.get_melee_width()

logger = logging.getLogger('RCScv')
logger.info('RCScv: Beginning Main')


ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, '..', 'resources')
def get_resource(name):
    return os.path.join(RESOURCES_DIR, name)

MELEE1 = get_resource('Melee1.png')
MELEE2 = get_resource('Melee2.png')
MELEE3 = get_resource('Melee3.jpg')
MELEE4 = get_resource('Melee4.jpg')
LETTERBOXED = get_resource('LetterboxedMelee.png')
CROPPED_LETTERBOX = get_resource('UnletterboxedMelee.png')

MELEE_FOOTAGE_GO = get_resource('GO.mp4')
MELEE_FOOTAGE_GAME = get_resource('GAME.mp4')

threader = Threader('rcsThreader', 5)

if __name__ == '__main__':
    video = MELEE_FOOTAGE_GAME
    print('Capturing %s' % video)
    print('Debug mode %s' % debug_mode)
    cap = cv2.VideoCapture(video)

    while(cap.isOpened()):
        ret, frame = cap.read()

        #When no more frames we are done
        if frame is None: 
            logger.info('Done!')
            break

        framecv = RCScv(cvimage=frame, output_name='frame.png')
        height = framecv.get_height()
        width = framecv.get_width()

        #If width of capture is more than X, cut off the letterboxing   
        if width > MELEE_WIDTH:
            letterbox_cropper.crop(framecv)

        if debug_mode is True:
            #Frame After Letterbox Processing
            framecv.show()

        #threader.run(stocks.do, framecv)
        stockDetection.run(framecv)
        
    cap.release()
    cv2.destroyAllWindows()