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
from util.config import Config
from lib import Common as common
from lib.croppers import percent_cropper as cropper

config = Config()

colors = []
for i in range(0, 4, 1):
    colors.append(common.random_color())

def draw(framecv, copy_tf=False):
    if copy_tf is True:
        copy = framecv.copy()
        cropper.drawBoxes(copy)
        copy.show()
    else:
        cropper.drawBoxes(framecv)

def do(framecv):
    copy = framecv.copy()
