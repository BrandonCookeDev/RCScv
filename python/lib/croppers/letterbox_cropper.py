import os, sys
import cv2
import logging
from interface import implements
from lib.Interfaces import ICropper
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()
crop = config.get_letterbox_crop()
left = crop['left']
right = crop['right']

class Letterbox_Cropper(implements(ICropper)):
    def crop(self, framecv):
        #Crop off the letterbox
        framecv.crop(None, None, left, right)

    def draw_rectangles(self, framecv):
        framecv.draw_rectangle(None, None, left, right)
