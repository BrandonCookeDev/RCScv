import os
from configparser import ConfigParser

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), '..', 'RCScv.config')

class Config(object):
    def __init__(self, file_path=DEFAULT_PATH):
        self.config = ConfigParser()
        self.config.read(file_path)

    def get_json_path(self):
        return str(self.config.get('program', 'json_path'))

    def get_frame_delay(self):
        return int(self.config.get('program', 'frame_delay'))

    def get_voter_threshold(self):
        return int(self.config.get('program', 'voter_threshold'))

    def get_melee_width(self):
        return int(self.config.get('melee', 'width'))

    def get_melee_height(self):
        return int(self.config.get('melee', 'height'))

    def get_melee_default_stocks(self):
        return int(self.config.get('melee', 'stocks'))

    def get_debug_mode(self):
        return bool(self.config.get('debug_mode', 'on') == 'True')

    def get_main_debug_mode(self):
        return bool(self.config.get('debug_mode', 'app') == 'True')

    def get_follow_stocks_debug_mode(self):
        return bool(self.config.get('debug_mode', 'follow_stocks') == 'True')

    def get_stock_cropper_debug_mode(self):
        return bool(self.config.get('debug_mode', 'stock_cropper') == 'True')

    def get_follow_stocks_buffer_size(self):
        return int(self.config.get('follow_stocks', 'buffer_size'))

    def get_follow_stocks_player_threshold(self):
        return int(self.config.get('follow_stocks', 'player_threshold'))

    def get_follow_stocks_non_player_threshold(self):
        return int(self.config.get('follow_stocks', 'non_player_threshold'))

    def get_letterbox_crop(self):
        return {
            'left': int(self.config.get('letterbox', 'left')),
            'right': int(self.config.get('letterbox', 'right'))
        }

    def get_canny_low_threshold_stocks(self):
        return int(self.config.get('stockscanny', 'lowthreshold'))

    def get_canny_high_threshold_stocks(self):
        return int(self.config.get('stockscanny', 'highthreshold'))

    def get_canny_thresholds_percent(self):
        return { 
            'high': int(self.config.get('percentcanny', 'highthreshold')),
            'low': int(self.config.get('percentcanny', 'lowthreshold'))
        }

    def get_timer(self):
        return {
            'top': int(self.config.get('timer', 'top')),
            'bottom': int(self.config.get('timer', 'bottom')),
            'left': int(self.config.get('timer', 'left')),
            'right': int(self.config.get('timer', 'right'))
        }

    def get_high_percent_canny(self):
        return int(self.config.get('percentcanny', 'lowthreshold'))

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

    def get_p1_percent(self):
        return {
            'top':int (self.config.get('p1percents', 'top')),
            'bottom':int (self.config.get('p1percents', 'bottom')),
            'left': int (self.config.get('p1percents', 'left')),
            'right':int (self.config.get('p1percents', 'right'))
        }

    def get_p2_percent(self):
        return {
            'top':int (self.config.get('p2percents', 'top')),
            'bottom':int (self.config.get('p2percents', 'bottom')),
            'left': int (self.config.get('p2percents', 'left')),
            'right':int (self.config.get('p2percents', 'right'))
        }
    def get_p3_percent(self):
        return {
            'top':int (self.config.get('p3percents', 'top')),
            'bottom':int (self.config.get('p3percents', 'bottom')),
            'left': int (self.config.get('p3percents', 'left')),
            'right':int (self.config.get('p3percents', 'right'))
        }

    def get_p4_percent(self):
        return {
            'top':int (self.config.get('p4percents', 'top')),
            'bottom':int (self.config.get('p4percents', 'bottom')),
            'left': int (self.config.get('p4percents', 'left')),
            'right':int (self.config.get('p4percents', 'right'))
        }

    def get_go_screen(self):
        return {
            'top': int(self.config.get('go_cropper', 'top')),
            'bottom': int(self.config.get('go_cropper', 'bottom')),
            'left': int(self.config.get('go_cropper', 'left')),
            'right': int(self.config.get('go_cropper', 'right'))
        }

    def get_game_screen(self):
        return {
            'top': int(self.config.get('game_cropper', 'top')),
            'bottom': int(self.config.get('game_cropper', 'bottom')),
            'left': int(self.config.get('game_cropper', 'left')),
            'right': int(self.config.get('game_cropper', 'right'))
        }