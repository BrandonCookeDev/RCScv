import os, sys
from interface import implements
from lib.RCScv import RCScv
from util.config import Config
from lib import Common as common
from lib.Interfaces import ICropper

config = Config()
game_screen = config.get_game_screen()
color = common.random_color()

class Game_Cropper(implements(ICropper)):
    
    def crop(self, framecv):
        framecv.crop(
            game_screen['top'], 
            game_screen['bottom'], 
            game_screen['left'], 
            game_screen['right']
        )

    def draw_rectangles(self, framecv):
        framecv.draw_rectangle(
            game_screen['top'], 
            game_screen['bottom'], 
            game_screen['left'], 
            game_screen['right'],
            color
        )
