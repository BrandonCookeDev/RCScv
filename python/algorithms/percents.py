import os, sys
import logging
from util.config import Config
from lib import Common as common
from lib.croppers import percent_cropper as cropper

config = Config()

colors = []
for i in range(0, 4, 1):
    colors.append(common.random_color())

def draw(framecv):
    copy = framecv.copy()
    cropper.drawBoxes(framecv)
    framecv.show()

def do(framecv):
    copy = framecv.copy()