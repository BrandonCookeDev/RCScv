import os, sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()

def crop_letterbox(frame):
    crop = config.get_letterbox_crop()
    left = crop['left']
    right = crop['right']

    #height = frame.shape[0]
    #width = frame.shape[1]

    game = RCScv(image_path=frame, output_name='gamecap.png')
    game.crop(None, None, left, right)
    return game
