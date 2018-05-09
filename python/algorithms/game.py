import os, sys
import logging
from util.config import Config
from lib.croppers import game_cropper as cropper

logger = logging.getLogger('RCScv')

config = Config()

def draw(framecv):
    copy = framecv.copy()
    cropper.draw_rectangles(copy)
    copy.show()

def do(framecv):
    copy = framecv.copy()
    cropper.crop(framecv)
    #copy.show()

