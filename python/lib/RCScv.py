import os, sys
import cv2 as cv
import copy as copy
import numpy as np
import random as random
import imutils as imutils

import logging
logger = logging.getLogger('RCScv')

class RCScv(object):

    def __init__(self, cvimage, output_name, image_path=None):
        if cvimage is None and image_path is None:
            raise Exception('image_path and cvimage cannot both be None for RCScv object')
        self.image_path = image_path

        if output_name is None:
            raise Exception('output_name cannot be None for RCScv obejct')
        self.output_name = output_name

        if cvimage is None:
            try:
                logger.info('loading image from path %s' % str(self.image_path))
                self.cvimage = cv.imread(self.image_path)
                self.cvoriginal = self.cvimage.copy()
            except Exception as e:
                logger.error(str(e))
                exit(1)
        else:
            self.cvimage = cvimage

    def copy(self):
        return copy.deepcopy(self)

    def get_cvimage(self):
        return self.cvimage 

    def get_height(self):
        return int(self.cvimage.shape[0])

    def get_width(self):
        return int(self.cvimage.shape[1])

    def save(self, output_name=None):
        if output_name is None:
            output_name = self.output_name

        logger.info('writting image to path %s' % output_name)
        cv.imwrite(output_name, self.cvimage)

    def crop(self, top, bottom, left, right):
        if top is None:
            top = 0
        if bottom is None:
            bottom = self.get_height()
        if left is None:
            left = 0
        if right is None:
            right = self.get_width()

        top     = int(top)
        bottom  = int(bottom)
        left    = int(left)
        right   = int(right)

        logger.info('cropping cvimage to [top %s, bottom %s, left %s, right %s]'
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
        hist = cv.calcHist([self.cvimage], [0], None, [256], [0, 256])
        return hist

    def show(self):
        logger.info('showing cvimage preview')
        cv.imshow('cvimage', self.cvimage)
        cv.waitKey()

    def detect_shape(self, contour):
        shape = "unidentified"
		#peri = cv.arcLength(contour, True)
        #approx = cv.approxPolyDP(contour, 0.04 * peri, True)

    def threshold(self, thresh):
        self.cvimage = cv.threshold(self.cvimage, thresh, 255, cv.THRESH_BINARY)[1]

    def get_contours(self):
        c = cv.findContours(self.cvimage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        c = c[0] if imutils.is_cv2() else c[1]
        return c

    def draw_contour(self, contour):
        cv.drawContours(self.cvimage, [contour], -1, random_color(), 2)

    def get_moments(self, contour):
        return cv.moments(contour)

    def gblur(self, sigmaX, sigmaY):
        self.cvimage = cv.GaussianBlur(self.cvimage, (sigmaX, sigmaY), 0)

    def draw_rectangle(self, top, bottom, left, right):
        logger.info('drawing rectangle [%s:%s] [%s:%s]' % (left, top, right, bottom))
        cv.rectangle(self.cvimage, (left, top), (right, bottom), random_color(), 2)

    def gauss_Blur(self, sigX, sigY):
        self.cvimage = cv.GaussianBlur(self.cvimage, (sigX, sigY), 0)

    def find_circles(self, circleArea=40):
        gray = cv.cvtColor(self.cvimage, cv.COLOR_BGR2GRAY)
        self.gauss_Blur(5,5)
        ret, thresh = cv.threshold(gray, 127, 255, 0)
        im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contourList = []
        for c in contours: 
            # obtains number of points found in figure, second argument is a accuracy parameter. Needs to be extremely small for small circles
            approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
            # print('Approx is ' + str(approx))
            area = cv.contourArea(c)
            if ((len(approx) > 6 and (area < circleArea))): contourList.append(c)
        self.cvimage = cv.drawContours(self.cvimage, contourList, -1, (0 , 0, 255), 2)
        self.show()
        return len(contourList) > 0

def random_color():
    return ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))