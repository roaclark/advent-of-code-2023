import os
import unittest
from .solution_2 import solution, solve

class TestSolution(unittest.TestCase):
  def test_solution_3(self):
    exp = 6
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_3.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()