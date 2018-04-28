import os, sys
import logging
import numpy
from lib import RCScv as cv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()

def process(cvimages, player_number):
    process_stock_images(cvimages, player_number)

def process_stock_images(cvimages, player_number):
    # Get black and white pixel distribution
    logger.debug('processing player %s', player_number)

    histograms = [img.get_histogram() for img in cvimages]

    pixel_threshold = config.get_stock_pixel_threshold()
    logger.debug('Player %s:' % player_number)
    for hist in histograms:
        black = hist[0][0]
        white = hist[255][0]

        logger.debug('black [%s] white [%s]' % (black, white))
    logger.debug('====================')