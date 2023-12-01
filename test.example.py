import os
import unittest
from .solution import solution, solve

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 100
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_solve(self):
    exp = 15
    act = solve([3, 1, 5])
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()