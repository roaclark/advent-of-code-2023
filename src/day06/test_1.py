import os
import unittest
from .solution_1 import solution, win_ways

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 288
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)
  
  def test_win_ways(self):
    self.assertEqual(4, win_ways(7, 9))
    self.assertEqual(8, win_ways(15, 40))
    self.assertEqual(9, win_ways(30, 200))

if __name__ == '__main__':
  unittest.main()