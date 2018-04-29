import os
import sys
import cv2
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

logger = logging.getLogger('RCScv')
config = Config()
#debug_mode = config.get_debug_mode()
debug_mode = config.get_stock_cropper_debug_mode()


def process_frame(frame):

    p1coords = config.get_p1_stocks()
    p1 = RCScv(image_path=None, cvimage=frame, output_name='p1frame.png')
    p1.crop(p1coords['top'], p1coords['bottom'],
            p1coords['left'], p1coords['right'])

    p1.greyscale()
    if debug_mode is True:
        p1.show()

    #p1.gblur(5, 5)
    #if debug_mode is True:
    #    p1.show()

    p1.threshold(100)
    if debug_mode is True:
        p1.show()

    s1 = get_individual_stocks(p1, p1coords)
    #p1_hist = p1.get_histogram()
    # print(p1_hist)

    p2coords = config.get_p2_stocks()
    p2 = RCScv(image_path=None, cvimage=frame, output_name='p2frame.png')
    p2.crop(p2coords['top'], p2coords['bottom'],
            p2coords['left'], p2coords['right'])

    p2.greyscale()
    if debug_mode is True:
        p2.show()

    #p2.gblur(5, 5)
    #if debug_mode is True:
        #p2.show()

    p2.threshold(100)
    if debug_mode is True:
        p2.show()

    s2 = get_individual_stocks(p2, p2coords)
    #p2_hist = p2.get_histogram()
    # print(p2_hist)

    p3coords = config.get_p3_stocks()
    p3 = RCScv(image_path=None, cvimage=frame, output_name='p2frame.png')
    p3.crop(p3coords['top'], p3coords['bottom'],
            p3coords['left'], p3coords['right'])

    p3.greyscale()
    if debug_mode is True:
        p3.show()

    #p3.gblur(5, 5)
    #if debug_mode is True:
        #p3.show()

    p3.threshold(100)
    if debug_mode is True:
        p3.show()

    s3 = get_individual_stocks(p3, p3coords)
    #p3_hist = p3.get_histogram()
    # print(p3_hist)

    p4coords = config.get_p4_stocks()
    p4 = RCScv(image_path=None, cvimage=frame, output_name='p2frame.png')
    p4.crop(p4coords['top'], p4coords['bottom'],
            p4coords['left'], p4coords['right'])

    p4.greyscale()
    if debug_mode is True:
        p4.show()

    #p4.gblur(5, 5)
    #if debug_mode is True:
        #p4.show()

    p4.threshold(100)
    if debug_mode is True:
        p4.show()

    s4 = get_individual_stocks(p4, p4coords)

    #p4_hist = p4.get_histogram()
    # print(p4_hist)

    return {
        "p1_stocks": s1,
        "p2_stocks": s2,
        "p3_stocks": s3,
        "p4_stocks": s4
    }


def draw_rectangles(frame):
    RCSframe = RCScv(cvimage=frame, output_name="test", image_path=None)

    p1coords = config.get_p1_stocks()
    p2coords = config.get_p2_stocks()
    p3coords = config.get_p3_stocks()
    p4coords = config.get_p4_stocks()

    logger.debug('rectangles at following coordinates \n [%s] \n [%s] \n [%s] \n [%s]'
                 % (p1coords, p2coords, p3coords, p4coords))

    RCSframe.rectangle(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'])
    RCSframe.rectangle(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'])
    RCSframe.rectangle(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'])
    RCSframe.rectangle(p4coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'])


def get_individual_stocks(stock_area, player):
    # Get stock contours
    contours = stock_area.get_contours()

    for contour in contours:
        try:
            M = stock_area.get_contour_moments(contour)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            contour = contour.astype("int")
            stock_area.draw_contour(contour)
        except Exception as e:
            logger.error(str(e))

    if debug_mode is True:
        stock_area.show()

def get_individual_stocks2(stock_area, coords):
    stocks = []

    height = stock_area.shape[0]
    width = stock_area.shape[1]

    default_low = config.get_canny_low_threshold_stocks()
    default_high = config.get_canny_high_threshold_stocks()

    division = width / 4

    stock_area.edge(default_low, default_high)
    if debug_mode is True:
        stock_area.show()

    left = 0
    for i in range(0, 4, 1):
        right = left + division
        stock = RCScv(cvimage=stock_area,
                      output_name='stocks.jpg', image_path=None)
        stock.crop(left=left, right=right, top=None, bottom=None)
        # stock.show()
        stocks.append(stock)
        left = right

    if debug_mode:
        [s.show() for s in stocks]

    return stocks
