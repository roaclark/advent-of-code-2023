import os
import unittest
from .solution_2 import solution, solve, number_from_line

class TestSolution(unittest.TestCase):
  def test_solution_1(self):
    exp = 142
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_1.txt'))
    self.assertEqual(exp, act)

  def test_solution_2(self):
    exp = 281
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_2.txt'))
    self.assertEqual(exp, act)

  def test_number_from_line(self):
    self.assertEqual(29, number_from_line('two1nine'))
    self.assertEqual(83, number_from_line('eightwothree'))
    self.assertEqual(13, number_from_line('abcone2threexyz'))
    self.assertEqual(24, number_from_line('xtwone3four'))
    self.assertEqual(42, number_from_line('4nineeightseven2'))
    self.assertEqual(14, number_from_line('zoneight234'))
    self.assertEqual(76, number_from_line('7pqrstsixteen'))
    self.assertEqual(82, number_from_line('eightwo'))

if __name__ == '__main__':
  unittest.main()