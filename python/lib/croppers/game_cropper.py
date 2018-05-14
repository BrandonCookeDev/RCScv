import os, sys
import logging
from interface import implements
from lib.RCScv import RCScv
from util.config import Config
from lib import Common as common
from lib.Interfaces import ICropper

config = Config()
game_screen = config.get_game_screen()
color = common.random_color()
logger = logging.getLogger('RCScv')

class Game_Cropper(implements(ICropper)):
    
    def crop(self, framecv):
        logger.debug('Game Cropper crop called [%s]' % framecv)
        assert framecv is not None, 'Game Cropper framecv cannot be None'
        assert isinstance(framecv, RCScv), 'Game Cropper framecv must be instance of RCScv'
        framecv.crop(
            game_screen['top'], 
            game_screen['bottom'], 
            game_screen['left'], 
            game_screen['right']
        )

    def draw_rectangles(self, framecv):
        logger.debug('Game Cropper draw rectangles called [%s]' % framecv)
        assert framecv is not None, 'Game Cropper framecv cannot be None'
        assert isinstance(framecv, RCScv), 'Game Cropper framecv must be instance of RCScv'
        framecv.draw_rectangle(
            game_screen['top'], 
            game_screen['bottom'], 
            game_screen['left'], 
            game_screen['right'],
            color
        )
