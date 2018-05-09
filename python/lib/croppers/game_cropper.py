import os, sys
from lib.RCScv import RCScv
from util.config import Config
from lib import Common as common

config = Config()
game_screen = config.get_game_screen()
color = common.random_color()

def crop(framecv):
    framecv.crop(
        game_screen['top'], 
        game_screen['bottom'], 
        game_screen['left'], 
        game_screen['right']
    )

def draw_rectangles(framecv):
    framecv.draw_rectangle(
        game_screen['top'], 
        game_screen['bottom'], 
        game_screen['left'], 
        game_screen['right'],
        color
    )