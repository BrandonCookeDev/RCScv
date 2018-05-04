import os, sys
import logging
from lib import RCScv as cv
from util.config import Config as Config
from lib import Models as m

logger = logging.getLogger('RCScv')
config = Config()

#buffer_size = config.get_follow_stocks_buffer_size()
player_threshold = config.get_follow_stocks_player_threshold()
non_player_threshold = config.get_follow_stocks_non_player_threshold()
debug_mode = config.get_follow_stocks_debug_mode()

# This buffer will hold x amount of frame data to perform calculations on
stock_image_buffers = m.FrameBuffer(config.get_follow_stocks_buffer_size())

def process(cvimages, player_number):
    process_stock_images(cvimages, player_number)

def process_stock_images(cvimages, player_number):
    # Get black and white pixel distribution
    logger.debug('processing player %s', player_number) #TODO change player_number to Player model and do stuff
    # TODO also, implement function that deactivates a player for a match so we reduce false positives

    histograms = [img.get_histogram() for img in cvimages]

    logger.debug('Player %s:' % player_number)
    for i in range(0, len(histograms), 1):
        # Get and log histogram
        hist = histograms[i]
        black = hist[0][0]
        white = hist[255][0]
        logger.debug('black [%s] white [%s]' % (black, white))

        # Generate key and cache the results for calculation
        # Then average the existing frame buffer for this player on this stock
        key_name = "P%sS%s" % (player_number, i)
        stock_image_buffer.add(key_name, white)
        avg = stock_image_buffer.average(key_name)
        logger.debug("%s average: %s" % (key_name, avg))

        # Deterministically rule out "non-players" ie empty controller ports
        # Deterministically rule is a present player has lost a stock
        #  by stating if the frames average below threshold and have enough frames
        #  for evidence that the player has definitively lost a stock
        if len(stock_image_buffers[key_name]) > buffer_size:
            if avg < non_player_threshold: pass
            elif avg < player_threshold:
                logger.warning('P%s has lost a stock!' % player_number)
    logger.debug('====================')

def add_to_stock_image_buffers(key, element):
    if key not in stock_image_buffers:
        stock_image_buffers[key] = []
    elif len(stock_image_buffers[key]) > buffer_size:
        del stock_image_buffers[key][0]
    stock_image_buffers[key].append(element)

def average_stock_image_buffers(key):
    assert stock_image_buffers[key] is not None, 'Null image buffer for key %s' % key

    sum = 0
    count = len(stock_image_buffers[key])
    for element in stock_image_buffers[key]:
        sum += element
    return sum/count
