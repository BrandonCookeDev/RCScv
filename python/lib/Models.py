import logging
from enum import Enum
from util.config import Config
from lib import Common as common

logger = logging.getLogger('RCScv')
config = Config()
default_stocks = config.get_melee_default_stocks

class game_states(Enum):
    STARTED = 1
    STOPPED = 2

class game_modes(Enum):
    SINGLES = 1
    DOUBLES = 2
    PAUSED = 3
    HAND_WARMER = 4


class Player(object):
    def __init__(self, tag=None, character=None, score=0, stocks=default_stocks):
        self.tag = tag
        self.character = character
        self.score = score
        self.stocks = stocks

    def increment_score(self):
        logger.debug('Player.increment_score called for %s' % self.tag)
        self.score += 1

    def decrement_score(self):
        logger.debug('Player.decrement_score called for %s' % self.tag)
        self.score -= 1

    def get_score(self):
        logger.debug('Player get score called')
        return self.score

    def get_character(self):
        logger.debug('Player get character called')
        return self.character

    def get_stocks(self):
        logger.debug('Player get stocks called')
        return self.stocks

    def set_score(self, new_score):
        logger.debug('Player.set_score called for %s [%s]' % (self.tag, new_score))
        assert new_score is not None, 'Player: new_score must not be None'
        assert isinstance(new_score, int),'Player: new_score must be instance of Integer'
        self.score = new_score

    def set_character(self, new_character):
        logger.debug('Player.set_character called for %s' % self.tag)
        assert new_character is not None, 'Player new_character must not be None'
        #TODO assert legal character and type
        self.character = new_character

    def set_stocks(self, new_stocks):
        logger.debug('Player.set_stocks called for %s [%s]' % (self.tag, new_stocks))
        assert new_stocks is not None, 'Player new_stocks must not be None'
        assert isinstance(new_stocks, int), 'Player: new_stocks must be instance of Integer'
        assert new_stocks >= 0 and new_stocks < 5, 'Player: new stocks must be between 0 and 5'
        self.stocks = new_stocks


class Match(object):
    def __init__(self, round=None, game_mode=None, best_of=3):
        self.round = round
        self.game_mode = game_mode
        self.best_of = best_of

    def get_round(self):
        logger.debug('Match get round called')
        return self.round

    def get_game_mode(self):
        logger.debug('Match get game mode called')
        return self.game_mode

    def get_best_of(self):
        logger.debug('Match get best of called')
        return self.best_of

    def set_round(self, new_round):
        logger.debug('Match set round of called [%s]' % new_round)
        assert new_round is not None, 'Match new_round must not be None'
        assert isinstance(new_round, str), 'Match new_round must be instance of string'
        self.round = new_round

    def set_game_mode(self, new_game_mode):
        logger.debug('Match get best of called')
        assert new_game_mode is not None, 'Match new_game_mode must not be None'
        assert isinstance(new_game_mode, game_modes), 'Match new_game_mode must be Enum game_modes'
        self.game_mode = new_game_mode

    def set_best_of(self, new_best_of):
        logger.debug('Match get best of called')
        assert new_best_of is not None, 'Match new_best_of must not be None'
        assert isinstance(new_best_of, int), 'Match new_best_of must be instance of Integer'
        self.best_of = new_best_of
        

class VoterBallot(object):
    def __init__(self, component_name, vote_weight,
                 p1_score=None, p1_stock_count=None, p2_score=None, 
                 p2_stock_count=None, game_mode=None, game_state=None):
        assert component_name is not None, 'VoterBallot: component name cannot be None'
        assert vote_weight is not None, 'VoterBallot: vote weight cannot be None'

        self.component_name = component_name
        self.vote_weight = vote_weight
        self.p1_score = p1_score
        self.p1_stock_count = p1_stock_count
        self.p2_score = p2_score
        self.p2_stock_count = p2_stock_count
        self.game_mode = game_mode
        self.game_state = game_state

    def __hash__(self):
        """
        Hash function. We only hash properties that will be similar in other
        VoterBallot objects. This is so equality checks can determine if the 
        hash of the meaninful values of the ballot are equal to another ballot's hash.

        NOTE: Because hashing integers only yields the integer itself, some ballots can
        resolve hashes similar to others with different values 
        ie:
            1^3^2^2 == 1^4^3^4

        ergo, the below implementation uses static strings to differentiate the values
        of different properties from each other and always generate a unique hash
            :param self: 
        """
        
        val = hash('p1_score: %s' % self.p1_score) \
            ^ hash('p1_stock_count: %s' % self.p1_stock_count) \
            ^ hash('p2_score: %s' % self.p2_score) \
            ^ hash('p2_stock_count: %s ' % self.p2_stock_count) \
            ^ hash(self.game_state) \
            ^ hash(self.game_mode) 
        logger.debug(val)
        return val

    def __eq__(self, other):
        """
        Equality check. We only check for match data properties to determine
        whether the vote this ballot represents is similar to another. We don't
        care about who submitted the ballot, that will matter later.
            :param self: 
            :param other: 
        """   
        
        val = isinstance(other, self.__class__)  \
            and self.p1_score == other.p1_score \
            and self.p1_stock_count == other.p1_stock_count \
            and self.p2_score == other.p2_score \
            and self.p2_stock_count == other.p2_stock_count \
            and self.game_mode == self.game_mode \
            and self.game_state == self.game_state
        return val


class VotingBox(object):
    def __init__(self, VoterBallots):
        assert isinstance(VoterBallots, list), 'VoterBallots must be instance of list'
        for ballot in VoterBallots:
            assert isinstance(ballot, VoterBallot), 'all elements in the VotingBox must be instance of VoterBallot'
        self.VoterBallots = VoterBallots

    def count_votes(self, voting_threshold):
        """
        Count Votes takes the overall ballots in the Voting Box
        and calculates the most likely results of the processed frame.
        This process is to implement checks and balances on the algorithm
        and reduce the margin of error produced by one or more algorithms 
        submitting incorrect results.

        Certain algorithms offer more weight in order to offset more 
        error-prone algorithms from asserting their analysis is correct.
            :param self: 
            :param voting_threshold: the peak difference where the popular vote trumps the weighted vote
        """   
        
        #gather the similar ballots into their repective segments (object properties)
        collection = {}
        for ballot in self.VoterBallots:
            if hash(ballot) in collection.__dict__:
                collection[hash(ballot)].append(ballot)
            else:
                collection[hash(ballot)] = [ballot]
        
        #Gather the popular vote 
        popular_vote = []
        for same_ballots in collection.__dict__:
            if len(collection[same_ballots]) > len(popular_vote):
                popular_vote = collection[same_ballots]

        #Gather the weighted vote
        electoral_college_weight = 0 
        electoral_college_vote = []
        for same_ballots in collection.__dict__:
            weight = 0
            for ballot in same_ballots: weight += ballot.vote_weight
            if weight > electoral_college_weight:
                electoral_college_vote = collection[same_ballots]

        #compare the vote types to make a decision
        difference = list(filter(lambda x: x not in popular_vote, electoral_college_vote))
        if len(difference) == 0:
            return electoral_college_vote
        else:
            if len(difference) > voting_threshold:
                return popular_vote
            else:
                return electoral_college_vote


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