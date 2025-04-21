import unittest
from bowling_game import BowlingGame  # Make sure this matches your actual import

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_sequence(self, sequence):
        for pins in sequence:
            self.game.roll(pins)

    def test_gutter_game(self):
        print("\nRunning: test_gutter_game")
        self.roll_many(20, 0)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(0, score)

    def test_all_ones(self):
        print("\nRunning: test_all_ones")
        self.roll_many(20, 1)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(20, score)

    def test_perfect_game(self):
        print("\nRunning: test_perfect_game")
        self.roll_many(12, 10)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(300, score)

    def test_all_spares(self):
        print("\nRunning: test_all_spares")
        self.roll_many(21, 5)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(150, score)

    def test_regular_game(self):
        print("\nRunning: test_regular_game")
        rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1, 7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
        self.roll_sequence(rolls)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(72, score)

    def test_mixed_game(self):
        print("\nRunning: test_mixed_game")
        rolls = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
        self.roll_sequence(rolls)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(190, score)

    def test_spare_bonus(self):
        print("\nRunning: test_spare_bonus")
        rolls = [5, 5, 3] + [0] * 17
        self.roll_sequence(rolls)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(16, score)

    def test_strike_bonus(self):
        print("\nRunning: test_strike_bonus")
        rolls = [10, 3, 4] + [0] * 17
        self.roll_sequence(rolls)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(24, score)

    def test_double_strike(self):
        print("\nRunning: test_double_strike")
        rolls = [10, 10, 4, 2] + [0] * 16
        self.roll_sequence(rolls)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(46, score)

    def test_10th_frame_bonus(self):
        print("\nRunning: test_10th_frame_bonus")
        rolls = [0] * 18 + [10, 10, 10]
        self.roll_sequence(rolls)
        score = self.game.score()
        print(f"Score: {score}")
        self.assertEqual(30, score)

if __name__ == '__main__':
    unittest.main()