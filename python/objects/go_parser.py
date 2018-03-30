import os, sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

class go_parser(object):
    def __init__(self, image_path, output_path, low_thresh=250, high_thresh=550, crop_x=None, crop_y=None):
        self.image_path = image_path
        self.output_path = output_path
        self.low_thresh = low_thresh
        self.high_thresh = high_thresh
        self.crop_x = crop_x
        self.crop_y = crop_y

        #property for the cv2 image object
        self.cv = cv2.imread(self.image_path, 0)
        self.cv_height = np.size(self.cv, 0)
        self.cv_width = np.size(self.cv, 1)

    def __str__(self):
        return 'go_parser: [%s] [%s] [%s] [%s] [%s] [%s]' % \
            (self.image_path, self.output_path, 
             self.low_thresh, self.high_thresh, 
             self.crop_x, self.crop_y)

    def do(self):
        print('cropping [%s] [%s]' % (self.crop_y, self.crop_x))
        self.crop()

        print('edging [%s] [%s]' % (self.low_thresh, self.high_thresh))
        edges = self.edges()
        
        print('writing to %s' % self.output_path)
        cv2.imwrite(self.output_path, edges)

    def crop(self):
        # todo assert crop_x and crop_y are valid subset arrays
        if(self.cv is not None):
            self.cv = self.cv[self.crop_y, self.crop_x]
        else:
            raise Exception('cv image cannot be null')

    def edges(self):
        if(self.cv is not None):
            edges = cv2.Canny(self.cv, self.low_thresh, self.high_thresh)
            return edges
        else:
            raise Exception('cv image cannot be null')
