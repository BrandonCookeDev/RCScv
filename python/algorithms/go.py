import os, sys
import logging
from lib import Models as M
from lib.detectors import detect_circles
from lib.croppers import go_cropper as cropper

logger = logging.getLogger('RCScv')

def do(framecv):
    copy = framecv.copy()
    cropper.crop(copy)

def draw(framecv):
    copy = framecv.copy()
    cropper.draw_rectangles(copy)
    copy.show()

def process_go_screen(framecv):
    pass