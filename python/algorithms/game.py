import os, sys
import logging
from interface import implements
from util.config import Config
from lib.croppers.game_cropper import Game_Cropper as Cropper
from lib.Interfaces import IAlgorithm

logger = logging.getLogger('RCScv')

config = Config()
cropper = Cropper()

class Game(implements(IAlgorithm)):
    def draw(self, framecv):
        copy = framecv.copy()
        cropper.draw_rectangles(copy)
        copy.show()

    def do(self, framecv):
        copy = framecv.copy()
        cropper.crop(framecv)
        #copy.show()

