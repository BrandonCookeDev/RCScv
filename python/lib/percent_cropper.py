# Name Jeff
import os, sys
import logging
from lib.RCScv import RCScv as RCScv
from util.config import Config as Config

def process_frame(frame): 
    print('we out here fam')
    p1 = RCScv(frame, 'p1frame.png')
    p1.show()