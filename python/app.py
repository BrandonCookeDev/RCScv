import os, sys
import cv2
import numpy
import logging
from util import log
from util.config import Config as Config
from lib.RCScv import RCScv as RCScv
from lib import stock_cropper
from lib import letterbox_cropper
from algorithms import follow_stocks

config = Config()
debug_mode = config.get_debug_mode()

logger = logging.getLogger('RCScv')
logger.info('RCScv: Beginning Main')

ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, '..', 'resources')
MELEE1 = os.path.join(RESOURCES_DIR, 'Melee1.png')
MELEE2 = os.path.join(RESOURCES_DIR, 'Melee2.png')
MELEE3 = os.path.join(RESOURCES_DIR, 'Melee3.jpg')
MELEE4 = os.path.join(RESOURCES_DIR, 'Melee4.jpg')
LETTERBOXED = os.path.join(RESOURCES_DIR, 'LetterboxedMelee.png')

MELEE_FOOTAGE1 = os.path.join(RESOURCES_DIR, 'GAME.mp4')
MELEE_FOOTAGE2 = os.path.join(RESOURCES_DIR, 'FullscreenMelee.mp4')

MELEE_HEIGHT = 584
MELEE_WIDTH = 480

if __name__ == '__main__':
    #c = stock_cropper.process_frame(MELEE3)
    #print(type(MELEE3))

    cap = cv2.VideoCapture(MELEE_FOOTAGE2)

    # just showing video to screen
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None: 
            logger.info('Done!')
            break

        height = frame.shape[0]
        width = frame.shape[1]

        if width > MELEE_WIDTH:
            frame = letterbox_cropper.crop_letterbox(frame)
        #cv2.imshow('frame', frame)
        print(type(frame))

        f = stock_cropper.process_frame(frame)
        stock_cropper.draw_rectangles(frame)
        if debug_mode is True: cv2.imshow('frame', frame)

        follow_stocks.process_histogram(f['p1_hist'], 1)
        follow_stocks.process_histogram(f['p2_hist'], 2)
        follow_stocks.process_histogram(f['p3_hist'], 3)
        follow_stocks.process_histogram(f['p4_hist'], 4)

    cap.release()
    cv2.destroyAllWindows()