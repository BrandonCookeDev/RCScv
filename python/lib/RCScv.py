import os, sys
import cv2 as cv
import copy as copy
import numpy as np
import random as random
import imutils as imutils
from lib import Common as common

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
        logger.debug('RCScv: copy called')
        return copy.deepcopy(self)

    def get_cvimage(self):
        logger.debug('RCScv: get cvimage')
        return self.cvimage 

    def get_height(self):
        logger.debug('RCScv: get height')
        return int(self.cvimage.shape[0])

    def get_width(self):
        logger.debug('RCScv: get width')
        return int(self.cvimage.shape[1])

    def save(self, output_name=None):
        if output_name is None:
            logger.debug('RCScv: save called [%s]' % output_name)
            output_name = self.output_name

        logger.info('writting image to path %s' % output_name)
        cv.imwrite(output_name, self.cvimage)

    def crop(self, top, bottom, left, right):
        logger.debug('RCScv: crop called [%s] [%s] [%s] [%s]' % (top, bottom, left, right))
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
        logger.info('RCScv: applying greyscale to cvimage')
        self.cvimage = cv.cvtColor(self.cvimage, cv.COLOR_BGR2GRAY)

    def edge(self, low_threshold, high_threshold):
        logger.debug('RCScv: applying canny edge algorithm to cvimage [%s] [%s]' % (low_threshold, high_threshold))
        self.cvimage = cv.Canny(self.cvimage, low_threshold, high_threshold)
    
    def get_histogram(self):
        logger.debug('RCScv: getting cvimage histogram')
        hist = cv.calcHist([self.cvimage], [0], None, [256], [0, 256])
        return hist

    def show(self):
        logger.debug('RCScv: showing cvimage preview')
        cv.imshow('cvimage', self.cvimage)
        cv.waitKey()

    def show_nowait(self):
        logger.debug('RCScv: showing cvimage preview')
        cv.imshow('cvimage', self.cvimage)

    def detect_shape(self, contour):
        logger.debug('RCScv: dected shape called')
        shape = "unidentified"
		#peri = cv.arcLength(contour, True)
        #approx = cv.approxPolyDP(contour, 0.04 * peri, True)

    def threshold(self, thresh):
        logger.debug('RCScv: threadhold called [%s]' % thresh)
        self.cvimage = cv.threshold(self.cvimage, thresh, 255, cv.THRESH_BINARY)[1]

    def get_contours(self):
        logger.debug('RCScv: get contours called')
        c = cv.findContours(self.cvimage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        c = c[0] if imutils.is_cv2() else c[1]
        return c

    def draw_contour(self, contour, color):
        logger.debug('RCScv: draw contours called [%s] [%s]' % (contour, color))
        if color is None:
            color = common.random_color()
        cv.drawContours(self.cvimage, [contour], -1, color, 2)

    def get_moments(self, contour):
        logger.debug('RCScv.get_moments [%s]' % contour)
        return cv.moments(contour)

    def gblur(self, sigmaX, sigmaY):
        logger.debug('RCScv.gblur [%s] [%s]' % (sigmaX, sigmaY))
        self.cvimage = cv.GaussianBlur(self.cvimage, (sigmaX, sigmaY), 0)
        
    def gauss_Blur(self, sigX, sigY):
        logger.debug('RCScv: guass_blur called [%s] [%s]' % (sigX, sigY))
        self.cvimage = cv.GaussianBlur(self.cvimage, (sigX, sigY), 0)

    def draw_rectangle(self, top, bottom, left, right, color=None):
        logger.debug('RCScv: draw rectangle called [%s] [%s] [%s] [%s] [%s]' % (top, bottom, left, right, color))
        if top is None:
            top = 0
        if bottom is None:
            bottom = self.get_height()
        if left is None:
            left = 0
        if right is None:
            right = self.get_width()

        if color is None:
            color = common.random_color()

        top     = int(top)
        bottom  = int(bottom)
        left    = int(left)
        right   = int(right)

        logger.info('RCScv: drawing rectangle [%s:%s] [%s:%s]' % (left, top, right, bottom))
        cv.rectangle(self.cvimage, (left, top), (right, bottom), color, 2)

    def find_circles2(self, minR=40, maxR=40):
        logger.debug('RCScv: find circles 2 called [%s] [%s]' % (minR, maxR))
        copy = self.copy()
        copy.greyscale()
        circles = cv.HoughCircles(copy.cvimage, cv.HOUGH_GRADIENT, minR, maxR)

        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
        
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv.circle(copy.cvimage, (x, y), r, (0, 255, 0), 4)
                cv.rectangle(copy.cvimage, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        
            # show the output image
            copy.show()
            #cv.imshow("output", np.hstack([self.cvimage, copy.cvimage]))
            #cv.waitKey(0)

    
    def find_circles(self, circleArea=40):
        logger.debug('RCScv: find circles called [%s]' % circleArea)
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

    def show_threshold(self, thresh=150, sigmaX=5, sigmaY=5):
        copy = self.copy()
        copy.greyscale()
        copy.gblur(sigmaX, sigmaY)
        copy.threshold(thresh)
        copy.show()

    def show_greyscale(self):
        copy = self.copy()
        copy.greyscale()
        copy.show()
    
    def show_gblur(self, sigmaX=5, sigmaY=5):
        copy = self.copy()
        copy.greyscale()
        copy.gblur(sigmaX, sigmaY)
        copy.show()
