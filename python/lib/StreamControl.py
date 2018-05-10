import os, sys, json
import logging
from enum import Enum
from lib.Models import Player
from lib.Models import Match
from util.config import Config

logger = logging.getLogger('RCScv')
config = Config()
default_stocks = config.get_melee_default_stocks()


class MatchData(object):
    __instance = None

    """
    Singleton object representing the current match happening in realtime
        :param object: 
    """
    def __new__(cls, Player1, Player2, Match):
        if MatchData.__instance is None:
            MatchData.__instance = object.__new__(cls)
        MatchData.__instance.Player1 = Player1
        MatchData.__instance.Player2 = Player2
        MatchData.__instance.Match = Match
        return MatchData.__instance

    @staticmethod
    def get_instance():
        logger.debug('MatchData get Instance called')
        return MatchData.__instance

    def reset(self):
        logger.debug('MatchData Reset called')
        MatchData.__instance.get_Player1.set_score(0)
        MatchData.__instance.get_Player2.set_score(0)
        MatchData.__instance.get_Player1.set_stocks(default_stocks)
        MatchData.__instance.get_Player2.set_stocks(default_stocks)        
        
    def get_Player1(self):
        logger.debug('MatchData get Player1 called')
        return MatchData.__instance.Player1

    def get_Player1(self):
        logger.debug('MatchData get Player2 called')
        return MatchData.__instance.Player2

    def get_Match(self):
        logger.debug('MatchData get Match called')
        return MatchData.__instance.Match

    def set_Player1(self, new_player1):
        logger.debug('MatchData.set_Player1 called [%s]' % new_player1)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_player1, Player), 'MatchData: new_player1 must be instance of Player'
        MatchData.__instance.Player1 = new_player1

    
    def set_Player2(self, new_player2):
        logger.debug('MatchData.set_Player2 called [%s]' % new_player2)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_player2, Player), 'MatchData: new_player2 must be instance of Player'
        MatchData.__instance.Player2 = new_player2


    def set_Match(self, new_match):
        logger.debug('MatchData.set_Match called [%s]' % new_match)
        assert MatchData.__instance is not None, 'MatchData.__instance cannot be None'
        assert isinstance(MatchData.__instance, MatchData), 'MatchData.__instance must be an instance of MatchData'
        assert isinstance(new_match, Match), 'MatchData: new_match must be instance of Match'
        MatchData.__instance.Match = new_match


class JSON_Peerer(object):
    def __init__(self, file_path, data):
        self.file_path = file_path
        self.data = data

    def read(self):
        logger.debug('JSON_Peerer.read called')
        contents = ''
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            print(data)
        
    def write(self, data):
        logger.debug('JSON_Peerer.write called [%s]' % data)

