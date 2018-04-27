import os, sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()
debug_mode = config.get_debug_mode()

def process_frame(frame):
    default_low = config.get_canny_low_threshold_stocks()
    default_high = config.get_canny_high_threshold_stocks()

    p1coords = config.get_p1_stocks()
    p1 = RCScv(image_path=None, cvimage=frame, output_name='p1frame.png')
    p1.crop(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'])
    p1.greyscale()
    p1.edge(default_low, default_high)
    if debug_mode is True: p1.show() 
    p1_hist = p1.get_histogram()
    #print(p1_hist)

    p2coords = config.get_p2_stocks()
    p2 = RCScv(image_path=None, cvimage=frame, output_name='p2frame.png')
    p2.crop(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'])
    p2.greyscale()
    p2.edge(default_low, default_high)
    if debug_mode is True: p2.show()
    p2_hist = p2.get_histogram()
    #print(p2_hist)

    p3coords = config.get_p3_stocks()
    p3 = RCScv(image_path=None, cvimage=frame, output_name='p2frame.png')
    p3.crop(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'])
    p3.greyscale()
    p3.edge(default_low, default_high)
    if debug_mode is True: p3.show()
    p3_hist = p3.get_histogram()
    #print(p3_hist)

    p4coords = config.get_p4_stocks()
    p4 = RCScv(image_path=None, cvimage=frame, output_name='p2frame.png')
    p4.crop(p4coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'])
    p4.greyscale()
    p4.edge(default_low, default_high)
    if debug_mode is True: p4.show()
    p4_hist = p4.get_histogram()
    #print(p4_hist)

    return {
        "p1_hist": p1_hist,
        "p2_hist": p2_hist,
        "p3_hist": p3_hist,
        "p4_hist": p4_hist
    }

def draw_rectangles(frame):
    p1coords = config.get_p1_stocks()
    p2coords = config.get_p2_stocks()
    p3coords = config.get_p3_stocks()
    p4coords = config.get_p4_stocks()

    logger.debug('rectangles at following coordinates \n [%s] \n [%s] \n [%s] \n [%s]'
        % (p1coords, p2coords, p3coords, p4coords))

    cv2.rectangle(frame, (p1coords['left'], p1coords['top']), (p1coords['right'], p1coords['bottom']), (255, 0, 0), 2)
    cv2.rectangle(frame, (p2coords['left'], p2coords['top']), (p2coords['right'], p2coords['bottom']), (0, 255, 0), 2)
    cv2.rectangle(frame, (p3coords['left'], p3coords['top']), (p3coords['right'], p3coords['bottom']), (0, 0, 255), 2)
    cv2.rectangle(frame, (p4coords['left'], p4coords['top']), (p4coords['right'], p4coords['bottom']), (255, 0, 255), 2)
