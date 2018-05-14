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
        logger.debug('Letterbox Cropper crop called [%s]' % framecv)
        assert framecv is not None, 'Letterbox Cropper framecv cannot be None'
        assert isinstance(framecv, RCScv), 'Letterbox Cropper framecv must be instance of RCScv'
        #Crop off the letterbox
        framecv.crop(None, None, left, right)

    def draw_rectangles(self, framecv):
        logger.debug('Letterbox Cropper draw rectangles called [%s]' % framecv)
        assert framecv is not None, 'Letterbox Cropper framecv cannot be None'
        assert isinstance(framecv, RCScv), 'Letterbox Cropper framecv must be instance of RCScv'
        framecv.draw_rectangle(None, None, left, right)
