import os, sys
import logging
from interface import implements
from lib import Models as M
from lib.detectors import detect_circles
from lib.croppers.go_cropper import Go_Cropper as Cropper
from lib.Interfaces import IAlgorithm

logger = logging.getLogger('RCScv')
cropper = Cropper()

class Go(implements(IAlgorithm)):
    def draw(self, framecv):
        copy = framecv.copy()
        cropper.draw_rectangles(copy)
        copy.show_nowait()

    def do(self, framecv):
        copy = framecv.copy()
        cropper.crop(copy)


    def process_go_screen(framecv):
        pass