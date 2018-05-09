import os, sys
from interface import implements
from lib.RCScv import RCScv
from util.config import Config
from lib import Common as common
from lib.Interfaces import ICropper

config = Config()
go_screen = config.get_go_screen()
color = common.random_color()

class Go_Cropper(implements(ICropper)):
    def crop(self, framecv):
        framecv.crop(
            go_screen['top'], 
            go_screen['bottom'], 
            go_screen['left'], 
            go_screen['right']
        )

    def draw_rectangles(self, framecv):
        framecv.draw_rectangle(
            go_screen['top'], 
            go_screen['bottom'], 
            go_screen['left'], 
            go_screen['right'],
            color
        )