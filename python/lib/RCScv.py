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
        hist = cv.calcHist([self.cvimage], [0], None, [256], [0, 256])
        return hist

    def show(self):
        logger.info('showing cvimage preview')
        cv.imshow('cvimage', self.cvimage)
        cv.waitKey()

    def draw_rectangle(self, top, bottom, left, right, rgb, thickness):
        cv.rectangle(self.cvimage, (left, top), (right, bottom), rgb, thickness)

    def gauss_Blur(self, sigX, sigY):
        self.cvimage = cv.GaussianBlur(self.cvimage, (sigX, sigY), 0)

# # Looks for circle with specified area. Defaults to optimal percent area (50)
#     def detect_circles(self, circleArea=50):
#         gray = cv.cvtColor(self.cvimage, cv.COLOR_BGR2GRAY)
#         self.gauss_Blur(5,5)
#         ret, thresh = cv.threshold(gray, 127, 255, 0)
#         im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#         contourList = []
#         for c in contours: 
#             # obtains number of points found in figure, second argument is a accuracy parameter. Needs to be extremely small for small circles
#             approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
#             # print('Approx is ' + str(approx))
#             area = cv.contourArea(c)
#             if ((len(approx) > 6 and (area < circleArea))): contourList.append(c)
#         self.cvimage = cv.drawContours(self.cvimage, contourList, -1, (0 , 0, 255), 2)
#         self.show()
#         return len(contourList) > 0