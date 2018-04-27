import os
from configparser import ConfigParser

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), '..', 'RCScv.config')

class Config(object):
    def __init__(self, file_path=DEFAULT_PATH):
        self.config = ConfigParser()
        self.config.read(file_path)

    def get_letterbox_crop(self):
        return {
            'left': int(self.config.get('letterbox', 'left')),
            'right': int(self.config.get('letterbox', 'right'))
        }

    def get_canny_low_threshold_stocks(self):
        return int(self.config.get('stockscanny', 'lowthreshold'))

    def get_canny_high_threshold_stocks(self):
        return int(self.config.get('stockscanny', 'highthreshold'))

    def get_p1_stocks(self):
        return {
            'top': int(self.config.get('p1stocks', 'top')),
            'bottom': int(self.config.get('p1stocks', 'bottom')),
            'left': int(self.config.get('p1stocks', 'left')),
            'right': int(self.config.get('p1stocks', 'right'))
        }

    def get_p2_stocks(self):
        return {
            'top': int(self.config.get('p2stocks', 'top')),
            'bottom': int(self.config.get('p2stocks', 'bottom')),
            'left': int(self.config.get('p2stocks', 'left')),
            'right': int(self.config.get('p2stocks', 'right'))
        }

    def get_p3_stocks(self):
        return {
            'top': int(self.config.get('p3stocks', 'top')),
            'bottom': int(self.config.get('p3stocks', 'bottom')),
            'left': int(self.config.get('p3stocks', 'left')),
            'right': int(self.config.get('p3stocks', 'right'))
        }
    
    def get_p4_stocks(self):
        return {
            'top': int(self.config.get('p4stocks', 'top')),
            'bottom': int(self.config.get('p4stocks', 'bottom')),
            'left': int(self.config.get('p4stocks', 'left')),
            'right': int(self.config.get('p4stocks', 'right'))
        }

    """
    BEGIN 480p
    """
    def get_p1_stocks_480(self):
        return {
            'top': int(self.config.get('p1stocks480', 'top')),
            'bottom': int(self.config.get('p1stocks480', 'bottom')),
            'left': int(self.config.get('p1stocks480', 'left')),
            'right': int(self.config.get('p1stocks480', 'right'))
        }

    def get_p2_stocks_480(self):
        return {
            'top': int(self.config.get('p2stocks480', 'top')),
            'bottom': int(self.config.get('p2stocks480', 'bottom')),
            'left': int(self.config.get('p2stocks480', 'left')),
            'right': int(self.config.get('p2stocks480', 'right'))
        }

    def get_p3_stocks_480(self):
        return {
            'top': int(self.config.get('p3stocks480', 'top')),
            'bottom': int(self.config.get('p3stocks480', 'bottom')),
            'left': int(self.config.get('p3stocks480', 'left')),
            'right': int(self.config.get('p3stocks480', 'right'))
        }
    
    def get_p4_stocks_480(self):
        return {
            'top': int(self.config.get('p4stocks480', 'top')),
            'bottom': int(self.config.get('p4stocks480', 'bottom')),
            'left': int(self.config.get('p4stocks480', 'left')),
            'right': int(self.config.get('p4stocks480', 'right'))
        }
