import os, sys, json
import logging
from enum import Enum
from Models import Player
from Models import Match

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
        assert isinstance(new_player1, Player), 'MatchData: new_player1 must be instance of Player'
        self.Player1 = new_player1
    
    def set_Player2(self, new_player2):
        logger.debug('MatchData.set_Player2 called [%s]' % new_player2)
        assert isinstance(new_player2, Player), 'MatchData: new_player2 must be instance of Player'
        self.Player2 = new_player2

    def set_Match(self, new_match):
        logger.debug('MatchData.set_Match called [%s]' % new_match)
        assert isinstance(new_match, Match), 'MatchData: new_match must be instance of Match'
        self.Match = new_match


class JSON_Peerer(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def read():
        logger.debug('JSON_Peerer.read called')
        contents = ''
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            print data
