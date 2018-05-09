import os
import sys
import cv2
import logging
from lib import Common as common
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

config = Config()
debug_mode = config.get_stock_cropper_debug_mode()
logger = logging.getLogger('RCScv')

colors = []
for i in range (0, 4, 1): 
    colors.append(common.random_color())

def draw_rectangles(framecv):
    p1coords = config.get_p1_stocks()
    p2coords = config.get_p2_stocks()
    p3coords = config.get_p3_stocks()
    p4coords = config.get_p4_stocks()

    logger.debug('rectangles at following coordinates \n [%s] \n [%s] \n [%s] \n [%s]'
                 % (p1coords, p2coords, p3coords, p4coords))

    framecv.draw_rectangle(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'], colors[0])
    framecv.draw_rectangle(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'], colors[1])
    framecv.draw_rectangle(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'], colors[2])
    framecv.draw_rectangle(p4coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'], colors[3])

def crop(framecv):
    p1 = framecv.copy()
    p1coords = config.get_p1_stocks()
    p1.crop(p1coords['top'], p1coords['bottom'],
            p1coords['left'], p1coords['right'])
    if debug_mode is True:
        p1.show()

    p2 = framecv.copy()
    p2coords = config.get_p2_stocks()
    p2.crop(p2coords['top'], p2coords['bottom'],
            p2coords['left'], p2coords['right'])
    if debug_mode is True:
        p2.show()

    p3 = framecv.copy()
    p3coords = config.get_p3_stocks()
    p3.crop(p3coords['top'], p3coords['bottom'],
            p3coords['left'], p3coords['right'])
    if debug_mode is True:
        p3.show()

    p4 = framecv.copy()
    p4coords = config.get_p4_stocks()
    p4.crop(p4coords['top'], p4coords['bottom'],
            p4coords['left'], p4coords['right'])
    if debug_mode is True:
        p4.show()

    return {
        "p1_stocks": p1,
        "p2_stocks": p2,
        "p3_stocks": p3,
        "p4_stocks": p4
    }

def get_individual_stocks(stock_area_cv):
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