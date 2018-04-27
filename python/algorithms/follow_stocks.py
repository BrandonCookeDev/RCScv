import os, sys
import logging
import numpy
from lib import RCScv as cv

logger = logging.getLogger('RCScv')

def process_histogram(hist, player_number):
    # Get black and white pixel distribution
    logger.debug('processing player %s', player_number)

    black = hist[0][0]
    white = hist[255][0]

    print('black [%s] white [%s]' % (black, white))
    logger.debug('black [%s] white [%s]' % (black, white))