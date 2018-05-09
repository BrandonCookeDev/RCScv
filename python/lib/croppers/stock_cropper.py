import os
import sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()
debug_mode = config.get_stock_cropper_debug_mode()

#TODO change to crop, move tranformative logic to algorithm
def process_frame(framecv):
    default_low = config.get_canny_low_threshold_stocks()
    default_high = config.get_canny_high_threshold_stocks()

    p1coords = config.get_p1_stocks()
    p1 = framecv.copy()
    p1.crop(p1coords['top'], p1coords['bottom'],
            p1coords['left'], p1coords['right'])
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
    s1 = get_individual_stocks(p1, p1coords)

    p2coords = config.get_p2_stocks()
    p2 = framecv.copy()
    p2.crop(p2coords['top'], p2coords['bottom'],
            p2coords['left'], p2coords['right'])
    p2.greyscale()
    p2.gblur(5, 5)
    p2.threshold(100)
    p2.edge(default_low, default_high)
    if debug_mode is True:
        p2.show()
    s2 = get_individual_stocks(p2, p2coords)

    p3coords = config.get_p3_stocks()
    p3 = framecv.copy()
    p3.crop(p3coords['top'], p3coords['bottom'],
            p3coords['left'], p3coords['right'])
    p3.greyscale()
    p3.gblur(5, 5)
    p3.threshold(100)
    p3.edge(default_low, default_high)
    if debug_mode is True:
        p3.show()
    s3 = get_individual_stocks(p3, p3coords)

    p4coords = config.get_p4_stocks()
    p4 = framecv.copy()
    p4.crop(p4coords['top'], p4coords['bottom'],
            p4coords['left'], p4coords['right'])
    p4.greyscale()
    p4.gblur(5, 5)
    p4.threshold(100)
    p4.edge(default_low, default_high)
    if debug_mode is True:
        p4.show()
    s4 = get_individual_stocks(p4, p4coords)

    return {
        "p1_stocks": s1,
        "p2_stocks": s2,
        "p3_stocks": s3,
        "p4_stocks": s4
    }


def draw_rectangles(framecv):
    p1coords = config.get_p1_stocks()
    p2coords = config.get_p2_stocks()
    p3coords = config.get_p3_stocks()
    p4coords = config.get_p4_stocks()

    logger.debug('rectangles at following coordinates \n [%s] \n [%s] \n [%s] \n [%s]'
                 % (p1coords, p2coords, p3coords, p4coords))

    framecv.draw_rectangle(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'])
    framecv.draw_rectangle(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'])
    framecv.draw_rectangle(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'])
    framecv.draw_rectangle(p4coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'])

def get_individual_stocks2(stock_area_cv):
    # Get stock contours
    contours = stock_area_cv.get_contours()

    for contour in contours:
        try:
            M = stock_area_cv.get_moments(contour)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            contour = contour.astype("int")
            stock_area_cv.draw_contour(contour)
        except Exception as e:
            logger.error(str(e))

    if debug_mode is True:
        stock_area_cv.show()

def get_individual_stocks(stock_area_cv, coords):
    stocks = []

    height = stock_area_cv.get_height()
    width = stock_area_cv.get_width()

    division = width / 4

    left = 0
    for i in range(0, 4, 1):
        right = left + division
        stock = stock_area_cv.copy()
        
        stock.crop(left=left, right=right, top=None, bottom=None)
        if debug_mode is True: stock.show()
        stocks.append(stock)
        left = right

    if debug_mode is True:
        [s.show() for s in stocks]

    return stocks
