# Name Jeff
import os, sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

config = Config()
logger = logging.getLogger()

def process_frame(frame): 
    print('we out here fam')
    # Initial test to draw boxes
    image = RCScv(frame, 'frame.png')
    drawBoxes(image)
    image.show()

    # get canny values
    percentCanny = config.get_canny_thresholds_percent()

    # Do timer stuff for the fans
    timer = RCScv(frame, 'timer.png')
    timercoords = config.get_timer()
    timer.crop(timercoords['top'], timercoords['bottom'], timercoords['left'], timercoords['right'])
    timer.greyscale
    timer.edge(percentCanny['low'], percentCanny['high'])
    timer.show()

    # Start cropping player percent signs
    p1 = RCScv(frame, 'p1frame.png')
    p1coords = config.get_p1_percent()
    p1.crop(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'])
    p1.greyscale()
    p1.gauss_Blur(5,5)
    p1.edge(percentCanny['low'], percentCanny['high'])
    p1.show()
    
    p1Hist = p1.get_histogram()
    

    p2 = RCScv(frame, 'p1frame.png')
    p2coords = config.get_p2_percent()
    p2.crop(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'])
    p2.greyscale()
    p2.gauss_Blur(5,5)
    p2.edge(percentCanny['low'], percentCanny['high'])
    p2.show()
   
    p2Hist = p2.get_histogram()
    

    p3 = RCScv(frame, 'p1frame.png')
    p3coords = config.get_p3_percent()
    p3.crop(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'])
    p3.greyscale()
    p3.gauss_Blur(5,5)
    p3.edge(percentCanny['low'], percentCanny['high'])
    p3.show()
    
    p3Hist = p3.get_histogram()
    

    p4 = RCScv(frame, 'p1frame.png')
    p4coords = config.get_p4_percent()
    p4.crop(p4coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'])
    p4.greyscale()
    p4.gauss_Blur(5,5)
    p4.edge(percentCanny['low'], percentCanny['high'])
    print('Logging p4 histagram: ' )
    p4.show()
    p4Hist = p4.get_histogram()
    


def drawBoxes(frame):
    # test out timer check
    timerCoord = config.get_timer()
    frame.draw_rectangle(timerCoord['top'], timerCoord['bottom'], timerCoord['left'], timerCoord['right'], (255,255,0))

    p1coords = config.get_p1_percent()
    frame.draw_rectangle(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'], (0, 0, 255))

    p2coords = config.get_p2_percent()
    frame.draw_rectangle(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'], (255, 0, 0))

    p3coords = config.get_p3_percent()
    frame.draw_rectangle(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'], (0, 255, 255))

    p4coords = config.get_p4_percent()
    frame.draw_rectangle(p3coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'], (0, 255, 0))
    

