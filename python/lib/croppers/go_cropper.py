import os, sys
from lib.RCScv import RCScv
from util.config import Config

config = Config()
go_screen = config.get_go_screen()

def crop_go(framecv):
    framecv.crop(
        go_screen['top'], 
        go_screen['bottom'], 
        go_screen['left'], 
        go_screen['right']
    )

def draw_box(framecv):
    framecv.draw_rectangle(
        go_screen['top'], 
        go_screen['bottom'], 
        go_screen['left'], 
        go_screen['right']
    )