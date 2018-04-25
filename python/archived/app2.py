from objects.go_parser import go_parser as parser

import os, sys
RESOURCES_DIR = os.path.join('..', 'resources')
GENERATED_DIR = os.path.join('.', 'generated')

melee_img = os.path.join(RESOURCES_DIR, 'meleeGOyoshis.jpg')
melee_img2 = os.path.join(RESOURCES_DIR, 'meleeGO.jpg')
smash4_img = os.path.join(RESOURCES_DIR, 'smash4GO.jpg')

melee_dark_rcs = os.path.join(RESOURCES_DIR, 'DarkMeleeGO.png')
melee_light_rcs = os.path.join(RESOURCES_DIR, 'LightMeleeGO.png')
smash4_rcs = os.path.join(RESOURCES_DIR, 'ArcadianGO.png')


if __name__ == '__main__':
    print('BEGIN Melee...')
    melee = parser(melee_img2, os.path.join(GENERATED_DIR, 'meleeGOEdges.jpg'),
                   crop_x1=450, crop_x2=1550, crop_y1=200, crop_y2=800)
    print(melee)
    melee.do()

    print('BEGIN Smash4...')
    smash4 = parser(smash4_img, os.path.join(GENERATED_DIR, 'smash4Edges.jpg'),
                    200, 550, crop_x1=400, crop_x2=1400, crop_y1=100, crop_y2=600)
    print(smash4)
    smash4.do()

    print('BEGIN RCS Melee Dark')
    rcs_melee_dark = parser(melee_dark_rcs, os.path.join(GENERATED_DIR, 'meleeDarkRCS.jpg'),
                            crop_x1=350, crop_x2=1100, crop_y1=200, crop_y2=650)
    print(rcs_melee_dark)
    rcs_melee_dark.do()

    print('BEGIN RCS Melee Light')
    rcs_melee_dark = parser(melee_light_rcs, os.path.join(GENERATED_DIR, 'meleeLightRCS.jpg'),
                            crop_x1=350, crop_x2=1100, crop_y1=200, crop_y2=650)
    print(rcs_melee_dark)
    rcs_melee_dark.do()

    #print('BEGIN RCS Smash 4')
    rcs_smash4 = parser(smash4_rcs, os.path.join(GENERATED_DIR, 'smash4RCS.jpg'),
                        200, 550, crop_x1=350, crop_x2=1150, crop_y1=150, crop_y2=500)
    print(rcs_smash4)
    rcs_smash4.do()


