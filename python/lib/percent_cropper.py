# Name Jeff
import os, sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

config = Config()
logger = logging.getLogger()

# Passing in MELEE2
def process_frame(frame): 
    print('we out here fam')
    #P2 will give better coordinates to begin for testing
    image = RCScv(frame, 'p1frame.png')
    drawBoxes(image)
    image.show()


def drawBoxes(frame):
    p1coords = config.get_p1_percent()
    frame.draw_rectangle(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'], (255, 0, 0), 2)

    p2coords = config.get_p2_percent()
    frame.draw_rectangle(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'], (0, 0, 255), 2)

    p3coords = config.get_p3_percent()
    frame.draw_rectangle(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'], (255, 255, 0), 2)

    p4coords = config.get_p4_percent()
    frame.draw_rectangle(p3coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'], (0, 255, 0), 2)
    

