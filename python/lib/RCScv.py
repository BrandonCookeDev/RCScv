import os, sys
import cv2 as cv
import numpy as np

import logging
logger = logging.getLogger('RCScv')

class RCScv(object):

    def __init__(self, image_path, output_name, cvimage=None):
        if image_path is None and cvimage is None:
            raise Exception('image_path cannot be None for RCScv object')
        self.image_path = image_path

        if output_name is None:
            raise Exception('output_name cannot be None for RCScv obejct')
        self.output_name = output_name

        if cvimage is None:
            try:
                logger.info('loading image from path %s' % str(self.image_path))
                self.cvimage = cv.imread(self.image_path)
            except Exception as e:
                logger.error(str(e))
                exit(1)
        else:
            self.cvimage = cvimage

    def get_cvimage(self):
        return self.cvimage 

    def save(self, output_name=None):
        if output_name is None:
            output_name = self.output_name

        logger.info('writting image to path %s' % output_name)
        cv.imwrite(output_name, self.cvimage)

    def crop(self, top=None, bottom=None, left=None, right=None):
        if top is None:
            top = 0
        if bottom is None:
            bottom = self.cvimage.shape[0]
        if left is None:
            left = 0
        if right is None:
            right = self.cvimage.shape[1]
            
        logger.info('cropping cvimage to follcalcHist([img], [0], None, [256], [0, 256])owing specs [top %s, bottom %s, left %s, right %s]'
                    % (top, bottom, left, right))

        top = int(top)
        bottom = int(bottom)
        left = int(left)
        right = int(right)

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
        hist = cv.calcHist([self.cvimage], [0], None, [256], [0, 256])
        return hist

    def show(self):
        logger.info('showing cvimage preview')
        cv.imshow('cvimage', self.cvimage)
        cv.waitKey()

    def draw_rectangle(self, top, bottom, left, right, rgb, thickness):
        logger.info('drawing rectangle [%s:%s] [%s:%s]' % (left, top, right, bottom))
        cv2.rectangle(self.cvimage, (left, top), (right, bottom), rgb, thickness)
    
