import os, sys, json
import logging
import keyboard
from enum import Enum
from lib import Models as M
from util.config import Config

logger = logging.getLogger('RCScv')
config = Config()
default_stocks = config.get_melee_default_stocks()
default_json_path = os.path.abspath(config.get_json_path())

class MatchData(object):
    __instance = None

    """
    Singleton object representing the current match happening in realtime
        :param object: 
    """
    def __new__(cls, Player1=M.Player(), Player2=M.Player(), Match=M.Match, State=M.game_states.STOPPED):
        if MatchData.__instance is None:
            MatchData.__instance = object.__new__(cls)

        assert Player1 is not None, 'MatchData Player1 cannot be None'
        assert Player2 is not None, 'MatchData Player2 cannot be None'
        assert Match is not None, 'MatchData Match cannot be None'
        assert State is not None, 'MatchData State cannot be None'
        assert isinstance(Player1, M.Player), 'MatchData Player1 must be instance of Player'
        assert isinstance(Player2, M.Player), 'MatchData Player2 must be instance of Player'
        assert isinstance(Match, M.Match), 'MatchData Match must be instance of Match'
        assert isinstance(State, M.game_states), 'MatchData State must be instance of game_states'

        MatchData.__instance.Player1 = Player1
        MatchData.__instance.Player2 = Player2
        MatchData.__instance.Match = Match
        MatchData.__instance.State = State
        return MatchData.__instance

    @staticmethod
    def get_instance():
        logger.debug('MatchData get Instance called')
        return MatchData.__instance

    def reset(self):
        logger.debug('MatchData Reset called')
        MatchData.__instance.get_Player1().set_score(0)
        MatchData.__instance.get_Player1().set_stocks(default_stocks)
        MatchData.__instance.get_Player2().set_score(0)
        MatchData.__instance.get_Player2().set_stocks(default_stocks)        
        
    def get_Player1(self):
        logger.debug('MatchData get Player1 called')
        return MatchData.__instance.Player1

    def get_Player2(self):
        logger.debug('MatchData get Player2 called')
        return MatchData.__instance.Player2

    def get_Match(self):
        logger.debug('MatchData get Match called')
        return MatchData.__instance.Match

    def get_State(self):
        logger.debug('MatchData get game state called')
        return MatchData.__instance.State

    def set_Player1(self, new_player1):
        logger.debug('MatchData.set_Player1 called [%s]' % new_player1)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_player1, M.Player), 'MatchData: new_player1 must be instance of Player'
        MatchData.__instance.Player1 = new_player1

    def set_Player2(self, new_player2):
        logger.debug('MatchData.set_Player2 called [%s]' % new_player2)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_player2, M.Player), 'MatchData: new_player2 must be instance of Player'
        MatchData.__instance.Player2 = new_player2

    def set_Match(self, new_match):
        logger.debug('MatchData.set_Match called [%s]' % new_match)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_match, M.Match), 'MatchData: new_match must be instance of Match'
        MatchData.__instance.Match = new_match

    def set_State(self, new_state):
        logger.debug('MatchData.set_game_state called [%s]' % new_state)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_state, M.game_states), 'MatchData: new_match must be instance of game_states'
        MatchData.__instance.State = new_state

class JSON_Peerer(object):
    def __init__(self, file_path=default_json_path, data={}):
        self.file_path = file_path
        self.data = data

    def set_data(self, data):
        assert data is not None, 'JSON peerer set, data cannot be none'
        assert isinstance(data, dict), 'JSON peerer set, data must be a dict'
        self.data = data

    def get_data(self):
        return self.data

    def read(self):
        logger.debug('JSON Reader.read called')
        with open(self.file_path, 'r') as f:
            content = f.readlines()
        content = ''.join(content)
        logger.debug('Got content from JSON %s' % content)

        data = json.loads(content)
        self.data = data
        logger.debug('JSON Reader Data %s' % self.data)
        return self.data
    
    def write(self, data):
        logger.debug('JSON_Peerer.write called [%s]' % data)
        assert data is not None, 'JSON Write data cannot be None'
        assert isinstance(data, dict), 'JSON Write data must be instance of dictionary'
        
        logger.debug('self data %s' % self.data)
        for key, val in self.data.items():
            logger.debug('self %s::%s' % (key, val))
            for new_key, new_val in data.items():
                logger.debug('%s::%s' % (key, val))
                if key == new_key:
                    self.data[key] = new_val

        new_json = json.dumps(self.data)
        with open(self.file_path, 'w') as f:
            f.write(new_json)
            logger.debug('JSON Writer wrote data %s' % self.data)

    def write_MatchData(self, data):
        logger.debug('JSON_Peerer.write called [%s]' % data)
        assert data is not None, 'JSON Write data cannot be None'
        assert isinstance(data, MatchData), 'JSON Write data must be instance of MatchData'
        
        for key, val in self.data.items():
            for new_key, new_val in data.items():
                if key == new_key:
                    self.data[key] = new_val

        new_json = json.dumps(self.data)
        with open(self.file_path, 'w') as f:
            f.write(new_json)
            logger.debug('JSON Writer wrote data %s' % self.data)


class Key_Combination(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.combo = ''
        for key in kwargs:
            combo += key + "+"
        #Remove overflow '+' character
        if len(combo) > 0: combo = combo[0:len(combo)] 
        
    @DeprecationWarning
    def verify_keys(self):
        pass


class Key_Presser(set):
    def add(self, element):
        logger.debug('Key Presser add called [%s]' % element)
        assert element is not None, 'Element must not be None for Key_Presser add'
        assert isinstance(element, Key_Combination), 'Element must be an instance of Key_Combination'
        super(Key_Presser, self).add(element)

    def get(self, name):
        logger.debug('Key Presser get called [%s]' % name)
        assert name is not None, 'name must not be None for Key Presser get'
        assert isinstance(name, str), 'name must be a string for Key Presser get'
        for element in self.iteritems():
            if element.name == name:
                return element.combo

    def press(self, name):
        logger.debug('Key Presser press called [%s]' % name)
        assert name is not None, 'name must not be None for Key Presser press'
        assert isinstance(name, str), 'name must be a string for Key Presser press'
        keyboard.press_and_release(self.get(name))