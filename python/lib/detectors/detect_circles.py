import os, sys
import cv2 as cv
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

config = Config()

# Looks for circle with specified area. Defaults to optimal percent area (50)
def find_circles(framecv, circleArea=40):
    gray = cv.cvtColor(framecv.cvimage, cv.COLOR_BGR2GRAY)
    framecv.gauss_Blur(5,5)
    ret, thresh = cv.threshold(gray, 127, 255, 0)
    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contourList = []
    for c in contours: 
        # obtains number of points found in figure, second argument is a accuracy parameter. Needs to be extremely small for small circles
        approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
        # print('Approx is ' + str(approx))
        area = cv.contourArea(c)
        if ((len(approx) > 6 and (area < circleArea))): contourList.append(c)
    framecv.cvimage = cv.drawContours(framecv.cvimage, contourList, -1, (0 , 0, 255), 2)
    framecv.show()
    return len(contourList) > 0

def detect_circles(frame):
    print('we out here fam')
    # Initial test to draw boxes
    image = RCScv(frame, 'frame.png')
    drawBoxes(image)
    image.show()

    # Start cropping player percent signs
    # Player 1
    p1 = RCScv(frame, 'p1frame.png')
    p1coords = config.get_p1_percent()
    p1.crop(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'])
    hasPercent = find_circles(p1)
    print(hasPercent)

    # Player 2
    p2 = RCScv(frame, 'p2frame.png')
    p2coords = config.get_p2_percent()
    p2.crop(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'])
    hasPercent = find_circles(p2)
    print(hasPercent)

    # Player 3 
    p3 = RCScv(frame, 'p2frame.png')
    p3coords = config.get_p3_percent()
    p3.crop(p2coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'])
    hasPercent = find_circles(p3)
    print(hasPercent)

    # Player 4
    p4 = RCScv(frame, 'p4frame.png')
    p4coords = config.get_p4_percent()
    p4.crop(p4coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'])
    hasPercent = find_circles(p4)
    print(hasPercent)


def drawBoxes(frame):
    # test out timer check
    timerCoord = config.get_timer()
    frame.draw_rectangle(timerCoord['top'], timerCoord['bottom'], timerCoord['left'], timerCoord['right'], (255,255,0), 2)

    p1coords = config.get_p1_percent()
    frame.draw_rectangle(p1coords['top'], p1coords['bottom'], p1coords['left'], p1coords['right'], (0, 0, 255), 2)

    p2coords = config.get_p2_percent()
    frame.draw_rectangle(p2coords['top'], p2coords['bottom'], p2coords['left'], p2coords['right'], (255, 0, 0), 2)

    p3coords = config.get_p3_percent()
    frame.draw_rectangle(p3coords['top'], p3coords['bottom'], p3coords['left'], p3coords['right'], (0, 255, 255), 2)

    p4coords = config.get_p4_percent()
    frame.draw_rectangle(p3coords['top'], p4coords['bottom'], p4coords['left'], p4coords['right'], (0, 255, 0), 2)



