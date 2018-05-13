import os, sys
import logging
from interface import implements
from lib import Models as M
from lib.detectors import detect_circles
from lib.croppers.go_cropper import Go_Cropper as Cropper
from lib.Interfaces import IAlgorithm
from lib.RCScv import RCScv

logger = logging.getLogger('RCScv')
cropper = Cropper()

class Go(implements(IAlgorithm)):
    def draw(self, framecv, copy_tf=False):
        assert framecv is not None, 'Go Algo: framecv must not be None'
        assert isinstance(framecv, RCScv), 'Go Algo: framecv must be instance of RCScv'
        assert isinstance(copy_tf, bool), 'Go Algo: copy_tf must be instance of bool'

        if copy_tf is True:
            copy = framecv.copy()
            cropper.draw_rectangles(copy)
            copy.show()
        else:
            cropper.draw_rectangles(framecv)

    def do(self, framecv):
        assert framecv is not None, 'Go Algo: framecv must not be None'
        assert isinstance(framecv, RCScv), 'Go Algo: framecv must be instance of RCScv'

        copy = framecv.copy()
        cropper.crop(copy)

        c = copy.find_circles(500)
        """
        copy.greyscale()
        copy.gblur(5,5)
        copy.threshold(100)
        """

        copy.show()
        
