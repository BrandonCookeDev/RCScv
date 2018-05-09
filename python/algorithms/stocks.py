import os, sys
import logging
from lib import RCScv as cv
from lib import Models as M
from lib.croppers import stock_cropper
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()

buffer_size = config.get_follow_stocks_buffer_size()
player_threshold = config.get_follow_stocks_player_threshold()
non_player_threshold = config.get_follow_stocks_non_player_threshold()
debug_mode = config.get_follow_stocks_debug_mode()

# This buffer will hold x amount of frame data to perform calculations on
stock_image_buffer = M.FrameBuffer(buffer_size)

def do(framecv):
    """
    thread running function to crop the frame and analyze the stocks
        :param rcscv: 
    """
    copy = framecv.copy()
    f = stock_cropper.process_frame(copy)
    stock_cropper.draw_rectangles(copy)
    if debug_mode is True:
        copy.show()

    process_stock_images(f['p1_stocks'], 1)
    process_stock_images(f['p2_stocks'], 2)
    process_stock_images(f['p3_stocks'], 3)
    process_stock_images(f['p4_stocks'], 4)

def draw(framecv):
    copy = framecv.copy()
    stock_cropper.draw_rectangles(copy)
    copy.show()

def process_stock_images(cvimages, player_number):
    # Get black and white pixel distribution
    logger = logging.getLogger('RCScv')
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
        if len(stock_image_buffer.get(key_name)) > buffer_size:
            if avg < non_player_threshold: pass
            elif avg < player_threshold:
                logger.warning('P%s has lost a stock!' % player_number)
    logger.debug('====================')