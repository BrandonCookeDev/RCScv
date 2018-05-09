import os, sys, json
import logging
from enum import Enum
from lib.Models import Player
from lib.Models import Match

logger = logging.getLogger('RCScv')

class MatchData(object):
    _instance = None

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

    def __init__(self, file_path):
        MatchData.__instance.file_path = file_path

    def read():
        logger.debug('JSON_Peerer.read called')
        contents = ''
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            print(data)
