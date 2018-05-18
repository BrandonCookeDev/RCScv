import os, sys
import logging
from lib import Models as M
from lib.RCScv import RCScv
from lib.Interfaces import IAlgorithm
from lib.detectors import detect_circles
from lib.croppers.go_cropper import Go_Cropper as Cropper
from interface import implements

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

        detected = False

        copy = framecv.copy()
        cropper.crop(copy)

        #copy.show_threshold(215)
        copy.threshold(215)
        #copy.find_circles2(500, 1000)
        copy.find_circles(8000)

        #if detected, we should make a ballot that the game has started
        if detected is True:
            state = M.game_states.STARTED
        else: 
            state = M.game_states.STOPPED
        ballot = M.VoterBallot(component_name='GO algorithm', vote_weight=3, game_state=state)
        return ballot
