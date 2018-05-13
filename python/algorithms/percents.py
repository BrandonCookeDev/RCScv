import os, sys
import logging
from lib import RCScv as cv
from lib import Models as M
from lib.croppers import percent_cropper
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()

def run(frame):
    print('We out here (again) fam')
