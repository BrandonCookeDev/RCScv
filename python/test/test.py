import sys, os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
print(path)
sys.path.insert(0, path)

import unittest

from lib import Models as M
from lib import StreamControl as SC

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
        self.p1 = M.Player(tag='cookiE', character='Sheik', score=0, stocks=4)
        self.p2 = M.Player(tag='Dog', character='Falco', score=3, stocks=3)
        self.m1 = M.Match(round='Winners Finals', game_mode=M.game_modes.SINGLES, best_of=5)
        self.MD = SC.MatchData(Player1=self.p1, Player2=self.p2, Match=self.m1)
        self.new_p = M.Player('Drax', 'Pikachu', 2, 1)
        self.new_m = M.Match('Crew Battle', M.game_modes.SINGLES, 20)

    def test_get_instance(self):
        self.md = SC.MatchData.get_instance()
        self.assertEqual(self.md, self.MD)

    def test_get_player1(self):
        self.assertEqual(self.MD.get_instance().get_Player1(), self.p1)

    def test_get_player2(self):
        self.assertEqual(self.MD.get_instance().get_Player2(), self.p2)
        
    def test_get_match(self):
        self.assertEqual(self.MD.get_instance().get_Match(), self.m1)

    def test_set_player1(self):
        self.MD.get_instance().set_Player1(self.new_p)
        self.assertEqual(self.MD.get_instance().Player1, self.new_p)

    def test_set_player2(self):
        self.MD.get_instance().set_Player2(self.new_p)
        self.assertEqual(self.MD.get_instance().Player2, self.new_p)

    def test_set_match(self):
        self.MD.get_instance().set_Match(self.new_m)
        self.assertEqual(self.MD.get_instance().Match, self.new_m)

    def test_reset(self):
        self.MD.get_instance().reset()
        self.assertEqual(self.MD.get_instance().Player1.score, 0)
        self.assertEqual(self.MD.get_instance().Player1.stocks, 4)
        self.assertEqual(self.MD.get_instance().Player2.score, 0)
        self.assertEqual(self.MD.get_instance().Player2.stocks, 4)

if __name__ == '__main__':
    unittest.main()