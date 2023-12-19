import os
import unittest
from .solution_1 import solution, solve

class TestSolution(unittest.TestCase):
  def test_solution_1(self):
    exp = 2
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_1.txt'))
    self.assertEqual(exp, act)

  def test_solution_1(self):
    exp = 6
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_2.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()