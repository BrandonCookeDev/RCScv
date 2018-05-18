import sys, os, json
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
print(path)
sys.path.insert(0, path)

import logging
import unittest
from lib import Models as M
from lib import StreamControl as SC

RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources')

class TestGameModes(unittest.TestCase):
    @unittest.skip("Will revist Enum with proper testing strategy")
    def test_game_modes(self):
        self.assertEqual(M.game_modes.SINGLES, 1)
        self.assertEqual(M.game_modes.DOUBLES, 2)
        self.assertEqual(M.game_modes.PAUSED, 3)
        self.assertEqual(M.game_modes.START, 4)
        self.assertEqual(M.game_modes.STOPPED, 5)
        self.assertEqual(M.game_modes.HAND_WARMER, 6)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        setup_logging('player')
        self.p1 = M.Player(tag='cookiE', character='Sheik', score=0, stocks=4)
        self.p2 = M.Player(tag='Dog', character='Falco', score=3, stocks=3)

    def test_get_score(self):
        self.assertEqual(self.p1.get_score(), 0)
        self.assertEqual(self.p2.get_score(), 3)

    def test_get_character(self):
        self.assertEqual(self.p1.get_character(), 'Sheik')
        self.assertEqual(self.p2.get_character(), 'Falco')

    def test_get_stocks(self):
        self.assertEqual(self.p1.get_stocks(), 4)
        self.assertEqual(self.p2.get_stocks(), 3)

    def test_increment_score(self):
        self.p1.increment_score()
        self.assertEqual(self.p1.score, 1)

        self.p1.increment_score()
        self.assertEqual(self.p1.score, 2)

    def test_decrement_score(self):
        self.p2.decrement_score()
        self.assertEqual(self.p2.score, 2)

        self.p2.decrement_score()
        self.assertEqual(self.p2.score, 1)

    def test_set_score(self):
        self.p1.set_score(5)
        self.p2.set_score(0)

        self.assertEqual(self.p1.score, 5)
        self.assertEqual(self.p2.score, 0)

    def test_set_character(self):
        self.p1.set_character('Fox')
        self.p2.set_character('Pichu')

        self.assertEqual(self.p1.character, 'Fox')
        self.assertEqual(self.p2.character, 'Pichu')

    def test_set_stocks(self):
        self.p1.set_stocks(1)
        self.p2.set_stocks(4)

        self.assertEqual(self.p1.stocks, 1)
        self.assertEqual(self.p2.stocks, 4)

class TestMatch(unittest.TestCase):
    def setUp(self):
        setup_logging('match')
        self.m1 = M.Match(round='Winners Finals', game_mode=M.game_modes.SINGLES, best_of=5)
        self.m2 = M.Match(round='Pools', game_mode=M.game_modes.DOUBLES, best_of=3)
    
    def test_get_round(self):
        self.assertEqual(self.m1.get_round(), 'Winners Finals')
        self.assertEqual(self.m2.get_round(), 'Pools')

    def test_get_game_mode(self):
        self.assertEqual(self.m1.get_game_mode(), M.game_modes.SINGLES)
        self.assertEqual(self.m2.get_game_mode(), M.game_modes.DOUBLES)

    def test_get_best_of(self):
        self.assertEqual(self.m1.get_best_of(), 5)
        self.assertEqual(self.m2.get_best_of(), 3)

    def test_set_round(self):
        self.m1.set_round('Grand Finals')
        self.m2.set_round('Winners Semis')

        self.assertEqual(self.m1.round, 'Grand Finals')
        self.assertEqual(self.m2.round, 'Winners Semis')

    def test_set_game_mode(self):
        self.m1.set_game_mode(M.game_modes.PAUSED)
        self.m2.set_game_mode(M.game_modes.HAND_WARMER)

        self.assertEqual(self.m1.game_mode, M.game_modes.PAUSED)
        self.assertEqual(self.m2.game_mode, M.game_modes.HAND_WARMER)

    def test_set_best_of(self):
        self.m1.set_best_of(7)
        self.m2.set_best_of(1)

        self.assertEqual(self.m1.best_of, 7)
        self.assertEqual(self.m2.best_of, 1)


class TestMatchData(unittest.TestCase):
    def setUp(self):
        setup_logging('match_data')
        self.p1 = M.Player(tag='cookiE', character='Sheik', score=0, stocks=4)
        self.p2 = M.Player(tag='Dog', character='Falco', score=3, stocks=3)
        self.m1 = M.Match(round='Winners Finals', game_mode=M.game_modes.SINGLES, best_of=5)
        self.s1 = M.game_states.STARTED
        self.state = M.game_states.STARTED
        self.MD = SC.MatchData(Player1=self.p1, Player2=self.p2, Match=self.m1, State=self.s1)
        self.new_p = M.Player('Drax', 'Pikachu', 2, 1)
        self.new_m = M.Match('Crew Battle', M.game_modes.SINGLES, 20)
        self.new_s = M.game_states.STOPPED

    def test_get_instance(self):
        self.md = SC.MatchData.get_instance()
        self.assertEqual(self.md, self.MD)

    def test_get_player1(self):
        self.assertEqual(self.MD.get_instance().get_Player1(), self.p1)

    def test_get_player2(self):
        self.assertEqual(self.MD.get_instance().get_Player2(), self.p2)
        
    def test_get_match(self):
        self.assertEqual(self.MD.get_instance().get_Match(), self.m1)

    def test_get_state(self):
        self.assertEqual(self.MD.get_instance().get_State(), self.s1)

    def test_set_player1(self):
        self.MD.get_instance().set_Player1(self.new_p)
        self.assertEqual(self.MD.get_instance().Player1, self.new_p)

    def test_set_player2(self):
        self.MD.get_instance().set_Player2(self.new_p)
        self.assertEqual(self.MD.get_instance().Player2, self.new_p)

    def test_set_match(self):
        self.MD.get_instance().set_Match(self.new_m)
        self.assertEqual(self.MD.get_instance().Match, self.new_m)

    def test_set_state(self):
        self.MD.get_instance().set_State(self.new_s)
        self.assertEqual(self.MD.get_instance().State, self.new_s)

    def test_reset(self):
        self.MD.get_instance().reset()
        self.assertEqual(self.MD.get_instance().Player1.score, 0)
        self.assertEqual(self.MD.get_instance().Player1.stocks, 4)
        self.assertEqual(self.MD.get_instance().Player2.score, 0)
        self.assertEqual(self.MD.get_instance().Player2.stocks, 4)


class TestJsonPeerer(unittest.TestCase):
    def setUp(self):
        setup_logging('json')
        self.json_path = os.path.join('.', 'data', 'test.json')
        self.jp = SC.JSON_Peerer(file_path=self.json_path)

        self.test_json_data = {
            "p1_name": "cookiE",
            "p1_games": "0",
            "p1_char": "Sheik",
            "p2_name": "Dog",
            "p2_games": "3",
            "p2_char": "Falco",
            "round": "Winners Finals",
            "best_of": "5",
            "tournament": "Tipped Off 12",
            "bracket": "https://smash.gg/to12"
        }
        self.jp.data = self.test_json_data

        with open(self.json_path, 'w') as f:
            s = json.dumps(self.test_json_data)
            f.write(s)

        self.test_json_data_2 = {
            "p1_name": "Baka4Moe",
            "p1_games": "0",
            "p1_char": "Peach",
            "p2_name": "RJW",
            "p2_games": "0",
            "p2_char": "Fox",
            "round": "Winners Semis",
            "best_of": "3",
            "tournament": "Tipped Off 12",
            "bracket": "https://smash.gg/to12"
        }

        self.test_json_data_3 = {
            "p1_name": "cookiE",
            "p1_games": "0",
            "p1_char": "Sheik",
            "p2_name": "Dog",
            "p2_games": "3",
            "p2_char": "Falco",
            "round": "Winners Finals",
            "best_of": "5",
            "tournament": "NaCl Omega",
            "bracket": "https://smash.gg/naclomega"
        }
    
        MD = SC.MatchData.get_instance()
    
    def test_get_data(self):
        self.assertEqual(self.jp.get_data(), self.test_json_data)


    def test_set_data(self):
        self.jp.set_data(self.test_json_data_2)
        self.assertEqual(self.jp.data, self.test_json_data_2)


    def test_read(self):
        self.assertEqual(self.jp.read(), self.test_json_data)


    def test_write_1(self):
        new_data = {
            "p1_name": "Baka4Moe",
            "p1_games": "0",
            "p1_char": "Peach",
            "p2_name": "RJW",
            "p2_games": "0",
            "p2_char": "Fox",
            "round": "Winners Semis",
            "best_of": "3"
        }
        self.jp.write(new_data)

        with open(self.json_path) as f:
            content = f.readlines()
        content = ''.join(content)
        
        data = json.loads(content)
        self.assertEqual(data, self.test_json_data_2)


    def test_write_2(self):
        new_data = {
            "tournament": "NaCl Omega",
            "bracket": "https://smash.gg/naclomega"
        }
        self.jp.write(new_data)

        with open(self.json_path) as f:
            content = f.readlines()
        content = ''.join(content)

        data = json.loads(content)
        self.assertEqual(data, self.test_json_data_3)

    def test_write_MD(self):
        pass


class TestVoterBallet(unittest.TestCase):
    def setUp(self):
        setup_logging('voter_ballet')
        self.v1 = M.VoterBallot(
            component_name='percent', 
            vote_weight=5, 
            p1_score=1, 
            p1_stock_count=3,
            p2_score=2,
            p2_stock_count=2,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STARTED
        )
        self.p1_1 = M.Player(score=1, stocks=3)
        self.p1_2 = M.Player(score=2, stocks=2)
        self.m1 = M.Match(game_mode=self.v1.game_mode)

        self.v2 = M.VoterBallot(
            component_name='stocks', 
            vote_weight=1, 
            p1_score=1, 
            p1_stock_count=3,
            p2_score=2,
            p2_stock_count=2,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STARTED
        )
        self.v3 = M.VoterBallot(
            component_name='go', 
            vote_weight=5, 
            p1_score=1, 
            p1_stock_count=4,
            p2_score=3,
            p2_stock_count=4,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STOPPED
        )
        self.p3_1 = M.Player(score=1, stocks=4)
        self.p3_2 = M.Player(score=3, stocks=4)
        self.m3 = M.Match(game_mode=self.v3.game_mode)

        self.v4 = M.VoterBallot(
            component_name='mode only',
            vote_weight=1,
            game_mode=M.game_modes.SINGLES
        )
        self.p4_1 = M.Player()
        self.p4_2 = M.Player()
        self.m4 = M.Match(game_mode=self.v4.game_mode)

        self.v5 = M.VoterBallot(
            component_name='mode only',
            vote_weight=1,
            game_state=M.game_states.STOPPED
        )
        self.p5_1 = M.Player()
        self.p5_2 = M.Player()
        self.m5 = M.Match()


    def test_eq(self):
        self.assertTrue(self.v1 == self.v2)
        self.assertFalse(self.v1 == self.v3)
        self.assertFalse(self.v2 == self.v3)

    def test_hash(self):
        self.assertEqual(hash(self.v1), hash(self.v2))
        self.assertNotEqual(hash(self.v1), hash(self.v3))
        self.assertNotEqual(hash(self.v2), hash(self.v3))

    def test_classify(self):
        self.assertEqual(self.v1.classify_ballot(), M.ballot_types.MATCH_DATA)
        self.assertEqual(self.v4.classify_ballot(), M.ballot_types.GAME_MODE_ONLY)
        self.assertEqual(self.v5.classify_ballot(), M.ballot_types.GAME_STATE_ONLY)

    def test_get_state(self):
        self.assertEqual(self.v1.get_game_state(), M.game_states.STARTED)
        self.assertEqual(self.v5.get_game_state(), M.game_states.STOPPED)

    def test_parse_player_objects_1(self):
        players = self.v1.parse_player_objects()
        self.assertTrue(len(players) == 2)

        self.assertEqual(players[0], self.p1_1)
        self.assertEqual(players[1], self.p1_2)

    def test_parse_player_objects_2(self):
        players = self.v3.parse_player_objects()
        self.assertTrue(len(players) == 2)

        self.assertEqual(players[0], self.p3_1)
        self.assertEqual(players[1], self.p3_2)

    def test_parse_player_objects_3(self):
        players = self.v4.parse_player_objects()
        self.assertTrue(len(players) == 2)

        print(str(players[0]))
        print(str(self.p4_1))
        self.assertEqual(players[0], self.p4_1)
        self.assertEqual(players[1], self.p4_2)

    def test_parse_match_object(self):
        self.assertEqual(self.v1.parse_match_object(), self.m1)
        self.assertEqual(self.v3.parse_match_object(), self.m3)
        self.assertEqual(self.v4.parse_match_object(), self.m4)
        self.assertEqual(self.v5.parse_match_object(), self.m5)

class TestVotingBox(unittest.TestCase):
    def setUp(self):
        setup_logging('voting_box')
        self.v1 = M.VoterBallot(
            component_name='percent', 
            vote_weight=5, 
            p1_score=1, 
            p1_stock_count=3,
            p2_score=2,
            p2_stock_count=2,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STARTED
        )
        self.v2 = M.VoterBallot(
            component_name='stocks', 
            vote_weight=1, 
            p1_score=1, 
            p1_stock_count=3,
            p2_score=2,
            p2_stock_count=2,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STARTED
        )
        self.v3 = M.VoterBallot(
            component_name='go', 
            vote_weight=3, 
            p1_score=1, 
            p1_stock_count=4,
            p2_score=3,
            p2_stock_count=4,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STARTED
        )
        self.v3 = M.VoterBallot(
            component_name='game', 
            vote_weight=2, 
            p1_score=2, 
            p1_stock_count=4,
            p2_score=3,
            p2_stock_count=4,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STARTED
        )
        self.v4 = M.VoterBallot(
            component_name='x',
            vote_weight=3, 
            p1_score=2, 
            p1_stock_count=4,
            p2_score=3,
            p2_stock_count=4,
            game_mode=M.game_modes.SINGLES,
            game_state=M.game_states.STOPPED
        )

        """
        Create boxes to handle different branches:
            1. Popular vote wins
            2. Weighted vote wins
            3. Popular and Weighted vote tie
        """

        self.box1 = M.VotingBox([self.v1, self.v2, self.v3, self.v4])
        self.box2 = M.VotingBox([self.v1, self.v4])

    def test_count_votes_1(self):
        pass



def setup_logging(name):
    LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', name + '_test.log')
    LOG_DIR = os.path.dirname(LOG_PATH)

    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)

    formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)-s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(LOG_PATH)
    handler.setFormatter(formatter)

    logger = logging.getLogger('RCScv')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.info('Logging setup for %s' % LOG_PATH)

if __name__ == '__main__':
    unittest.main()