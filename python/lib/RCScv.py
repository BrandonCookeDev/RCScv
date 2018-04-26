import os, sys
import cv2 as cv
import numpy as np

import logging
logger = logging.getLogger('RCScv')

class RCScv(object):

    def __init__(self, image_path, output_name):
        if image_path is None:
            raise Exception('image_path cannot be None for RCScv object')
        self.image_path = image_path

        if output_name is None:
            raise Exception('output_name cannot be None for RCScv obejct')
        self.output_name = output_name

        try:
            logger.info('loading image from path %s' % str(self.image_path))
            self.cvimage = cv.imread(self.image_path)
        except Exception as e:
            logger.error(str(e))
            exit(1)

    def get_cvimage(self):
        return self.cvimage 

    def save(self):
        logger.info('writting image to path %s' % self.output_name)
        cv2.imwrite(self.output_path, self.cvimage)

    def crop(self, top, bottom, left, right):
        logger.info('cropping cvimage to follcalcHist([img], [0], None, [256], [0, 256])owing specs [top %s, bottom %s, left %s, right %s]'
                    % (top, bottom, left, right))

        assert top < bottom, 'Top crop must be smaller than the bottom crop'
        assert left < right, 'Left crop must be smaller than the right crop'

        self.cvimage = self.cvimage[top:bottom, left:right]

    def greyscale(self):
        logger.info('applying greyscale to cvimage')
        self.cvimage = cv.cvtColor(self.cvimage, cv.COLOR_BGR2GRAY)

    def edge(self, low_threshold, high_threshold):
        logger.info('applying canny edge algorithm to cvimage')
        self.cvimage = cv.Canny(self.cvimage, low_threshold, high_threshold)
    
    def get_histogram(self):
        logger.info('getting cvimage histogram')
        hist = calcHist([self.cvimage], [0], None, [256], [0, 256])
        return hist

    def show(self):
        logger.info('showing cvimage preview')
        cv.imshow('cvimage', self.cvimage)
