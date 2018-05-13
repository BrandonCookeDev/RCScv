import os, sys
import logging
from lib.detectors import detect_circles

logger = logging.getLogger('RCScv')

def do(framecv):
    copy = framecv.copy()