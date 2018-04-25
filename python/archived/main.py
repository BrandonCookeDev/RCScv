from objects.go_parser import go_parser as parser

import cv2
import os, sys
RESOURCES_DIR = os.path.join('..', 'resources')
GENERATED_DIR = os.path.join('.', 'generated')

melee_img = os.path.join(RESOURCES_DIR, 'meleeGOyoshis.jpg')
melee_img2 = os.path.join(RESOURCES_DIR, 'meleeGO.jpg')
smash4_img = os.path.join(RESOURCES_DIR, 'smash4GO.jpg')

melee_dark_rcs = os.path.join(RESOURCES_DIR, 'DarkMeleeGO.png')
melee_light_rcs = os.path.join(RESOURCES_DIR, 'LightMeleeGO.png')
smash4_rcs = os.path.join(RESOURCES_DIR, 'ArcadianGO.png')

go_video = os.path.join(RESOURCES_DIR, 'GO.mp4')

if __name__ == "__main__":

    cap = cv2.VideoCapture(go_video)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if(frame is None):
            pass

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()