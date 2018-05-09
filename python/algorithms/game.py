import os, sys
import logging
from util.Config import Config
from lib.croppers import game_cropper as cropper

logger = logging.getLogger('RCScv')

config = Config()

def do(framecv):
    copy = framecv.copy()
    cropper.crop(framecv)
    #copy.show()

def draw(framecv):
    copy = framecv.copy()
    cropper.draw_rectangles(copy)
    copy.show()

