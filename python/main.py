from objects.go_parser import go_parser as parser

import os, sys
RESOURCES_DIR = os.path.join('..', 'resources')
melee_img = os.path.join(RESOURCES_DIR, 'meleeGOyoshis.jpg')
melee_img2 = os.path.join(RESOURCES_DIR, 'meleeGO.jpg')
smash4_img = os.path.join(RESOURCES_DIR, 'smash4GO.jpg')

if __name__ == '__main__':
    print('BEGIN Melee...')
    melee = parser(melee_img2, 'meleeGOEdges.jpg', crop_x1=450, crop_x2=1550, crop_y1=200, crop_y2=800)
    print(melee)
    melee.do()

    print('BEGIN Smash4...')
    smash4 = parser(smash4_img, 'smash4Edges.jpg', crop_x1=400, crop_x2=1400, crop_y1=100, crop_y2=600)
    print(smash4)
    smash4.do()