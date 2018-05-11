import cv2
import os, sys
import logging
from interface import implements
from lib import RCScv as cv
from lib import Models as M
from lib.RCScv import RCScv
from lib.Interfaces import IAlgorithm
from lib.StreamControl import MatchData as MD
from lib.croppers.stock_cropper import Stock_Cropper as Cropper
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()
cropper = Cropper()

buffer_size = config.get_follow_stocks_buffer_size()
player_threshold = config.get_follow_stocks_player_threshold()
non_player_threshold = config.get_follow_stocks_non_player_threshold()
debug_mode = config.get_follow_stocks_debug_mode()

default_high = config.get_canny_high_threshold_stocks()
default_low = config.get_canny_low_threshold_stocks()

match_data = MD.get_instance()

# This buffer will hold x amount of frame data to perform calculations on
stock_image_buffer = M.FrameBuffer(buffer_size)

class Stocks(implements(IAlgorithm)):
    def draw(self, framecv, copy_tf=False):
        assert framecv is not None, 'Stocks Algo: framecv must not be None'
        assert isinstance(framecv, RCScv), 'Stocks Algo: framecv must be instance of RCScv'
        assert isinstance(copy_tf, bool), 'Stocks Algo: copy_tf must be instance of bool'

        if copy_tf is True:
            copy = framecv.copy()
            cropper.draw_rectangles(copy)
            copy.show()
        else:
            cropper.draw_rectangles(framecv)
            

    def do(self, framecv):
        assert framecv is not None, 'Stocks Algo: framecv must not be None'
        assert isinstance(framecv, RCScv), 'Stocks Algo: framecv must be instance of RCScv'

        """
        thread running function to crop the frame and analyze the stocks
            :param rcscv: 
        """

        copy = framecv.copy()
        players = cropper.crop(copy)

        p1 = players['p1_stocks'].copy()
        p1.find_circles()
        p1.show()

        p1.greyscale()
        p1.gblur(5, 5)
        if debug_mode is True:
            p1.show()
        p1.threshold(100)
        if debug_mode is True:
            p1.show()
        p1.edge(default_low, default_high)
        if debug_mode is True:
            p1.show()
        s1 = cropper.get_individual_stocks(p1)

        p2 = players['p2_stocks'].copy()
        p2.greyscale()
        p2.gblur(5, 5)
        p2.threshold(100)
        p2.edge(default_low, default_high)
        if debug_mode is True:
            p2.show()
        s2 = cropper.get_individual_stocks(p2)

        p3 = players['p3_stocks'].copy()
        p3.greyscale()
        p3.gblur(5, 5)
        p3.threshold(100)
        p3.edge(default_low, default_high)
        if debug_mode is True:
            p3.show()
        s3 = cropper.get_individual_stocks(p3)

        p4 = players['p4_stocks'].copy()
        p4.greyscale()
        p4.gblur(5, 5)
        p4.threshold(100)
        p4.edge(default_low, default_high)
        if debug_mode is True:
            p4.show()
        s4 = cropper.get_individual_stocks(p4)

        #TODO return something
        

    def process_stock_images(self, cvimages, player_number, stock_number):
        assert cvimages is not None, 'Stock process stock images: cvimages must not be None'
        assert player_number is not None, 'Stock process stock images: player_number must not be None'
        assert isinstance(player_number, int), 'Stock process stock images: player_number must be an integer'
        assert stock_number > 0 and stock_number < 5, 'stock_number must be 1-4'

        # Get black and white pixel distribution
        logger = logging.getLogger('RCScv')
        logger.debug('processing player %s', player_number) #TODO change player_number to Player model and do stuff
        # TODO also, implement function that deactivates a player for a match so we reduce false positives

        histograms = [img.get_histogram() for img in cvimages]

        logger.debug('Player %s:' % player_number)
        for i in range(1, len(histograms) + 1, 1):

            #If we want a certain stock, this logic targets that
            if stock_number is not None and i != stock_number: 
                continue

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