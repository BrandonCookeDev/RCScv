import os, sys
import logging
from interface import implements
from lib.RCScv import RCScv
from lib.Interfaces import IAlgorithm
from lib.croppers.game_cropper import Game_Cropper as Cropper

logger = logging.getLogger('RCScv')
cropper = Cropper()

class Game(implements(IAlgorithm)):
    def draw(self, framecv, copy_tf=False):
        assert framecv is not None, 'Game Algo: framecv must not be None'
        assert isinstance(framecv, RCScv), 'Game Algo: framecv must be instance of RCScv'
        assert isinstance(copy_tf, bool), 'Game Algo: copy_tf must be instance of bool'

        if copy_tf is True:
            copy = framecv.copy()
            cropper.draw_rectangles(copy)
            copy.show()
        else:
            cropper.draw_rectangles(framecv)

    def do(self, framecv):
        assert framecv is not None, 'Game Algo: framecv must not be None'
        assert isinstance(framecv, RCScv), 'Game Algo: framecv must be instance of RCScv'

        copy = framecv.copy()
        cropper.crop(framecv)
        

