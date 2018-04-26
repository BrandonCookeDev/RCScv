import os, sys
import cv2
import numpy
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

MELEE_FOOTAGE1 = os.path.join(RESOURCES_DIR, 'GAME.mp4')

if __name__ == '__main__':
    #c = stock_cropper.process_frame(MELEE3)
    #print(type(MELEE3))

    cap = cv2.VideoCapture(MELEE_FOOTAGE1)

    # just showing video to screen
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        print(type(frame))

        c = stock_cropper.process_frame(frame)

        #cv2.waitKey()
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

    cap.release()
    cv2.destroyAllWindows()
    
