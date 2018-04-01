import os, sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

class go_parser(object):
    def __init__(self, image_path, output_path, low_thresh=250, high_thresh=550,
                        crop_y1=None, crop_y2=None, crop_x1=None, crop_x2=None):
        self.image_path = image_path
        self.output_path = output_path
        self.low_thresh = low_thresh
        self.high_thresh = high_thresh
        self.crop_x1 = crop_x1
        self.crop_x2 = crop_x2
        self.crop_y1 = crop_y1
        self.crop_y2 = crop_y2

        #property for the cv2 image object
        self.cv = cv2.imread(self.image_path, 0)
        self.cv_height = np.size(self.cv, 0)
        self.cv_width = np.size(self.cv, 1)

        if(self.crop_x1 is None):
            self.crop_x1 = 0
        if(self.crop_x2 is None):
            self.crop_x2 = self.cv_width
        if(self.crop_y1 is None):
            self.crop_y1 = 0
        if(self.crop_y2 is None):
            self.crop_y2 = self.cv_height

    def __str__(self):
        return 'go_parser: [%s] [%s] [%s] [%s] [%s:%s] [%s:%s]' % \
            (self.image_path, self.output_path, 
             self.low_thresh, self.high_thresh, 
             self.crop_x1, self.crop_x2,
             self.crop_y1, self.crop_y2)

    def do(self):
        print('cropping [%s:%s] [%s:%s]' % (self.crop_y1, self.crop_y2, self.crop_x1, self.crop_x2))
        self.crop()

        print('edging [%s] [%s]' % (self.low_thresh, self.high_thresh))
        edges = self.edges()
        
        print('writing to %s' % self.output_path)
        cv2.imwrite(self.output_path, edges)

    def crop(self):
        # todo assert crop_x and crop_y are valid subset arrays
        if(self.cv is not None):
            self.cv = self.cv[self.crop_y1:self.crop_y2, self.crop_x1:self.crop_x2]
        else:
            raise Exception('cv image cannot be null')

    def edges(self):
        if(self.cv is not None):
            edges = cv2.Canny(self.cv, self.low_thresh, self.high_thresh)
            return edges
        else:
            raise Exception('cv image cannot be null')

    def compare(self, frame):
        if(self.cv is not None):
            output = self.load_output_file()
            output_hist = go_parser.hist(output)
            frame_hist = go_parser.hist(frame)

            diff = cv2.compareHist(output_hist, frame_hist, cv2.HISTCMP_BHATTACHARYYA)
            return diff
        else:
            raise Exception('cv image cannot be null')

    def load_output_file(self):
        try:
            img = cv2.imread(self.output_path, 0)
            return img
        except:
            try:
                self.do()
                img = cv2.imread(self.output_path, 0)
                return img
            except Exception as e:
                print(e);
                sys.exit(1)

    @staticmethod
    def hist(img):
        return cv2.calcHist([img], [0], None, [256], [0, 256])