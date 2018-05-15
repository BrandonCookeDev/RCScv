import unittest

from lib import Models as M
from lib import StreamControl as SC

class TestGameModes(unittest.TestCase):
    def test_game_modes():
        self.assertEqual(M.game_modes.SINGLES, 1)
        self.assertEqual(M.game_modes.DOUBLES, 2)
        self.assertEqual(M.game_modes.PAUSED, 3)
        self.assertEqual(M.game_modes.START, 4)
        self.assertEqual(M.game_modes.STOPPED, 5)
        self.assertEqual(M.game_modes.HAND_WARMER, 6)

class TestPlayer(unittest.TestCase):
    def setUp():
        p1 = M.Player(tag='cookiE', character='Sheik', score=0, stocks=4)
        p2 = M.Player(tag='Dog', character='Falco', score=3, stocks=3)

    def test_get_score():
        self.assertEqual(p1.get_score(), 0)
        self.assertEqual(p2.get_score(), 3)

    def test_get_character():
        self.assertEqual(p1.get_character(), 'Sheik')
        self.assertEqual(p2.get_character(), 'Falco')

    def test_get_stocks():
        self.assertEqual(p1.get_stocks(), 4)
        self.assertEqual(p2.get_stocks(), 3)

    def test_increment_score():
        p1.increment_score()
        self.assertEqual(p1.score, 1)

        p1.increment_score()
        self.assertEqual(p1.score, 2)

    def test_decrement_score():
        p2.decrement_score()
        self.assertEqual(p2.score, 2)

        p2.decrement_score()
        self.assertEqual(p2.score, 1)

    def test_set_score():
        p1.set_score(5)
        p2.set_score(0)

        self.assertEqual(p1.score, 5)
        self.assertEqual(p2.score, 0)

    def test_set_character():
        p1.set_character('Fox')
        p2.set_character('Pichu')

        self.assertEqual(p1.character, 'Fox')
        self.assertEqual(p2.character, 'Pichu')

    def test_set_stocks():
        p1.set_stocks(1)
        p2.set_stocks(4)

        self.assertEqual(p1.stocks, 1)
        self.assertEqual(p2.stocks, 4)

class TestMatch(unittest.Test):
    def setUp():
        m1 = M.Match(round='Winners Finals', game_mode=M.game_modes.SINGLES, best_of=5)
        m2 = M.Match(round='Pools', game_mode=M.game_modes.DOUBLES, best_of=3)
    
    def test_get_round():
        self.assertEqual(m1.get_round, 'Winners Finals')
        self.assertEqual(m2.get_round, 'Pools')

    def test_get_game_mode():
        self.assertEqual(m1.get_game_mode, M.game_modes.SINGLES)
        self.assertEqual(m2.get_game_mode, M.game_modes.DOUBLES)

    def test_get_best_of():
        self.assertEqual(m1.get_best_of, 5)
        self.assertEqual(m2.get_best_of, 3)

    def test_set_round():
        m1.set_round('Grand Finals')
        m2.set_round('Winners Semis')

        self.assertEqual(m1.round, 'Grand Finals')
        self.assertEqual(m2.round, 'Winners Semis')

    def test_set_game_mode():
        m1.set_game_mode(M.game_modes.PAUSED)
        m2.set_game_mode(M.game_modes.HAND_WARMER)

        self.assertEqual(m1.game_mode, M.game_modes.PAUSED)
        self.assertEqual(m2.game_mode, M.game_modes.HAND_WARMER)

    def test_set_best_of():
        m1.set_best_of(7)
        m2.set_best_of(1)

        self.assertEqual(m1.best_of, 7)
        self.assertEqual(m2.best_of, 1)


class TestMatchData(unittest.TestCase):
    def setUp():
        p1 = M.Player(tag='cookiE', character='Sheik', score=0, stocks=4)
        p2 = M.Player(tag='Dog', character='Falco', score=3, stocks=3)
        m1 = M.Match(round='Winners Finals', game_mode=M.game_modes.SINGLES, best_of=5)
        MD = SC.MatchData(Player1=p1, Player2=p2, Match=m1)
        new_p = Player('Drax', 'Pikachu', 2, 1)
        new_m = Match('Crew Battle', M.game_modes.SINGLES, 20)

    def test_get_instance():
        md = SC.MatchData.get_instance()
        self.assertEqual(md, SC.MatchData.__instance)
        self.assertEqual(md, MD)

    def test_get_player1():
        self.assertEqual(MD.get_instance.get_Player1(), p1)

    def test_get_player2():
        self.assertEqual(MD.get_instance.get_Player2(), p2)
        
    def test_get_match():
        self.assertEqual(MD.get_instance.get_Match(), m)

    def test_set_player1():
        MD.get_instance.set_Player1(new_p)
        self.assertEqual(MD.get_instance.Player1, new_p)

    def test_set_player2():
        MD.get_instance.set_Player2(new_p)
        self.assertEqual(MD.get_instance.Player2, new_p)

    def test_set_match():
        MD.get_instance.set_Match(new_m)
        self.assertEqual(MD.get_instsance.Match, new_m)

    def test_reset():
        MD.get_instance.reset()
        self.assertEqual(MD.get_instance.Player1.score, 0)
        self.assertEqual(MD.get_instance.Player1.stocks, 4)
        self.assertEqual(MD.get_instance.Player2.score, 0)
        self.assertEqual(MD.get_instance.Player2.stocks, 4)

if __name__ == '__main__':
    unittest.main()