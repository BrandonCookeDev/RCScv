import os, sys
import logging
import RCScv 

logger = getLogger('RCScv')

def process_frame(frame):
    frame_cv = RCScv(framecv)
    frame_cv.crop(355, 390, 10, 140)
    frame_cv.show()