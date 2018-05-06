import os, sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()

def crop_letterbox(framecv):
    crop = config.get_letterbox_crop()
    left = crop['left']
    right = crop['right']

    #height = frame.shape[0]
    #width = frame.shape[1]
    
    #Crop off the letterbox
    framecv.crop(None, None, left, right)
