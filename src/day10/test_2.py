import os
import unittest
from .solution_2 import solution, solve

class TestSolution(unittest.TestCase):
  def test_solution_1(self):
    exp = 1
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_1.txt'))
    self.assertEqual(exp, act)

  def test_solution_2(self):
    exp = 1
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_2.txt'))
    self.assertEqual(exp, act)

  def test_solution_3(self):
    exp = 4
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_3.txt'))
    self.assertEqual(exp, act)

  def test_solution_4(self):
    exp = 4
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_4.txt'))
    self.assertEqual(exp, act)

  def test_solution_5(self):
    exp = 8
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_5.txt'))
    self.assertEqual(exp, act)

  def test_solution_6(self):
    exp = 10
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_6.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()