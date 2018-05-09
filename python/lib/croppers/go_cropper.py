import os, sys
from lib.RCScv import RCScv
from util.config import Config
from lib import Common as common

config = Config()
go_screen = config.get_go_screen()
color = common.random_color()

def crop(framecv):
    framecv.crop(
        go_screen['top'], 
        go_screen['bottom'], 
        go_screen['left'], 
        go_screen['right']
    )

def draw_rectangles(framecv):
    framecv.draw_rectangle(
        go_screen['top'], 
        go_screen['bottom'], 
        go_screen['left'], 
        go_screen['right'],
        color
    )