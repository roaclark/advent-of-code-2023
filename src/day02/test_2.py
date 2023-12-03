import os
import unittest
from .solution_1 import parse_game
from .solution_2 import solution, solve, game_product

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 2286
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_game_product(self):
    self.assertEqual(48, game_product(parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')))
    self.assertEqual(12, game_product(parse_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')))
    self.assertEqual(1560, game_product(parse_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')))
    self.assertEqual(630, game_product(parse_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')))
    self.assertEqual(36, game_product(parse_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')))


if __name__ == '__main__':
  unittest.main()