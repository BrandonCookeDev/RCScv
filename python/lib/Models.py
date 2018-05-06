import logging
from enum import Enum

logger = logging.getLogger('RCScv')

class Player(object):
    def __init__(self, tag, character, score):
        self.tag = tag
        self.character = character
        self.score = score

    def increment_score():
        logger.debug('Player.increment_score called for %s' % self.tag)
        self.score += 1

    def decrement_score():
        logger.debug('Player.decrement_score called for %s' % self.tag)
        self.score -= 1

    def set_score(new_score):
        logger.debug('Player.set_score called for %s' % self.tag)
        assert isinstance(new_score, int),'Player: new_score must be instance of Integer'
        self.score = new_score

    def set_character(new_character):
        logger.debug('Player.set_character called for %s' % self.tag)
        #TODO assert legal character and type
        self.character = new_character


class Match(object):
    def __init__(self, round, game_mode, best_of):
        self.round = round
        self.game_mode = game_mode
        self.best_of = best_of

class game_modes(Enum):
    SINGLES = 1
    DOUBLES = 2
    PAUSED = 3
    START = 4
    STOPPED = 5
    HAND_WARMER = 6

class FrameBuffer(object):
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

    def add(self, key, val):
        """
        FrameBuffer add will add an object property to an object and set it to 
        an array with the value specified in it. If the array at the property name
        exists and is over the length specified by self.buffer_size, element 0 will
        be popped from the array at the property.

        example: 
        self.buffer_size = 7
        {
            "P1S1": [55, 66, 44, 78, 65, 43, 23]
            "P1S2": [33, 66, 22, 11, 23, 43, 14]
            "P1S3": [55, 66, 44, 78, 23]
        }
        add("PS1S", 67)
        add("PS3S", 69)
        yields
        {
            "P1S1": [66, 44, 78, 65, 43, 23, 67] #55 removed, queue shifts left, 67 is added
            "P1S2": [33, 66, 22, 11, 23, 43, 14]
            "P1S3": [55, 66, 44, 78, 23, 69]     #69 added because len < self.buffer_size
        }

            :param self: this object
            :param key: name for the object property this will be stored at
            :param val: value to be stored in the array at `name`
        """   
        logger.debug('FrameBuffer.add called [%s] [%s]' % (key, val))

        assert key is not None, 'FrameBuffer.add: Key may not be None'
        assert val is not None, 'FrameBuffer.add: Val may not be None'

        if key not in self.__dict__:
            self.__dict__[key] = []
        elif len(self.__dict__[key]) > self.buffer_size:
            del self.__dict__[key][0]
        self.__dict__[key].append(val)
        
    def pop(self, key):
        """
        FrameBuffer pop removes the first element from the array at the specified
        property name, and returns that value to the caller
            :param self: this object
            :param key: name of the property owning the array to pop first element
        """   
        logger.debug('FrameBuffer.pop called [%s]' % key)

        assert key is not None, 'FrameBuffer.pop key cannot be None'
        assert key in self, 'FrameBuffer.pop key must be a property of FrameBuffer object'

        val = self.__dict__[key][0]
        del self.__dict__[key][0]
        return val

    def get_index(self, key, index):
        """
        FrameBuffer get_index retrieves the element at the specified property name and array index
        and returns it to the caller
            :param self: this object
            :param key: property name owning the target array
            :param index: array index of the desired element
        """   
        logger.debug('FrameBuffer.get_index called [%s] [%s]' % (key, index))

        assert key is not None, 'FrameBuffer.get key cannot be None'
        assert key in self, 'FrameBuffer.get key must be a property of FrameBuffer object'
        assert index is not None, 'FrameBuffer.get index cannot be None'
        assert len(self.__dict__[key]) > index, 'FrameBuffer.get index is out of range for the array at key %s' % key

        val = self.__dict__[key][index]
        return val

    def get(self, key):
        """
        FrameBuffer get returns the array value at the given property name
            :param self: this object
            :param key: property name owning the target array
        """   
        logger.debug('FrameBuffer.get called [%s]' % key)

        assert key is not None, 'FrameBuffer.get key cannot be None'
        assert key in self.__dict__, 'FrameBuffer.get key must be a property of FrameBuffer object'

        val = self.__dict__[key]
        return val

    def remove_index(self, key, index):
        """
        FrameBuffer remove_index deletes a value from the array owned by the given property name
        at the given index
            :param self: this object
            :param key: property name owning the target array
            :param index: array index of the desired element
        """
        logger.debug('FrameBuffer.remove_index called [%s] [%s]' % (key, index))

        assert key is not None, 'FrameBuffer.get key cannot be None'
        assert key in self.__dict__, 'FrameBuffer.get key must be a property of FrameBuffer object'
        assert index is not None, 'FrameBuffer.get index cannot be None'
        assert len(self.__dict__[key]) > index, 'FrameBuffer.get index is out of range for the array at key %s' % key

        del self.__dict__[key][index]

    def remove(self, key):
        """
        FrameBuffer remove returns the array value at the given property name
            :param self: this object
            :param key: property name owning the target array
        """   
        logger.debug('FrameBuffer.remove called [%s]' % key)

        assert key is not None, 'FrameBuffer.get key cannot be None'
        assert key in self.__dict__, 'FrameBuffer.get key must be a property of FrameBuffer object'

        del self.__dict__[key]

    def average(self, key):
        """
        FrameBuffer average takes a property name, and returns the average of
        the values in the array located at that property name 
            :param self: this object
            :param key: name of the property owning the array to be averaged
        """   
        logger.debug('FrameBuffer.average called [%s]' % key)

        assert self.__dict__[key] is not None, 'Null image buffer for key %s' % key

        sum = 0
        count = len(self.__dict__[key])
        for element in self.__dict__[key]:
            sum += element
        return sum/count

"""
class Melee_Characters(Enum):
    Fox = 1
	Falco = 2
    Sheik = 3
    Marth = 4
	Captain_Falcon  = 5
    Jigglypuff  = 6
    Ice_Climbers  = 7
    Peach = 8
	Pikachu = 9
    Samus = 10
	Dr_Mario = 11
    Yoshi  = 12
    Luigi = 13
	Mario = 14
    Link  = 15
    Young_Link  = 16
    Donkey_Kong  = 17
    Ganondorf = 18
	Roy = 19
    Mr_Game_and_Watch  = 20
    Mewtwo  = 21
    Zelda  = 22
    Ness = 23
	Pichu  = 24
    Bowser  = 25
    Kirby = 26
"""