import os, sys
import logging
from interface import implements
from lib.RCScv import RCScv
from lib.RCScv import RCScv
from lib.Interfaces import ICropper
from lib import Common as common
from util.config import Config

config = Config()
go_screen = config.get_go_screen()
color = common.random_color()
logger = logging.getLogger('RCScv')

class Go_Cropper(implements(ICropper)):
    def crop(self, framecv):
        logger.debug('Go Cropper crop called [%s]' % framecv)
        assert framecv is not None, 'Go Cropper framecv cannot be None'
        assert isinstance(framecv, RCScv), 'Go Cropper framecv must be instance of RCScv'
        framecv.crop(
            go_screen['top'], 
            go_screen['bottom'], 
            go_screen['left'], 
            go_screen['right']
        )

    def draw_rectangles(self, framecv):
        logger.debug('Go Cropper draw rectangles called [%s]' % framecv)
        assert framecv is not None, 'Go Cropper framecv cannot be None'
        assert isinstance(framecv, RCScv), 'Go Cropper framecv must be instance of RCScv'
        framecv.draw_rectangle(
            go_screen['top'], 
            go_screen['bottom'], 
            go_screen['left'], 
            go_screen['right'],
            color
        )
