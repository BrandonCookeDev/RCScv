from objects.go_parser import go_parser as parser

import os, sys
RESOURCES_DIR = os.path.join('..', 'resources')
melee_img = os.path.join(RESOURCES_DIR, 'meleeGOyoshis.jpg')
melee_img2 = os.path.join(RESOURCES_DIR, 'meleeGO.jpg')
smash4_img = os.path.join(RESOURCES_DIR, 'smash4GO.jpg')

if __name__ == '__main__':
    print('BEGIN...')
    melee = parser(melee_img2, 'meleeImg2Edges.jpg')
    print(melee)
    melee.do()
