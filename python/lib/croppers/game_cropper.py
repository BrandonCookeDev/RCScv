import os, sys
from lib.RCScv import RCScv
from util.config import Config

config = Config()
game_screen = config.get_game_screen()

def crop_go(imagecv):
    framecv.crop(
        game_screen['top'], 
        game_screen['bottom'], 
        game_screen['left'], 
        game_screen['right']
    )

def draw_box(imagecv):
    framecv.draw_rectangle(
        game_screen['top'], 
        game_screen['bottom'], 
        game_screen['left'], 
        game_screen['right']
    )