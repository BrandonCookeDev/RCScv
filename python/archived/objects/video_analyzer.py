import os, sys
import cv2
import numpy as np

class video_analyzer(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.cap = cv2.VideoCapture(0)

    def frame_by_frame(self):
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()