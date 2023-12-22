import os
import unittest
from .solution_1 import parse_input, get_expanded_distances

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(grid):
  return get_expanded_distances(grid, 1000000)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

class TestSolution(unittest.TestCase):
  def test_get_expanded_distances_1(self):
    test_filepath = os.path.join(os.path.dirname(__file__), 'test_input.txt')
    act = get_expanded_distances(parse_input(test_filepath), 10)
    exp = 1030
    self.assertEqual(exp, act)

  def test_get_expanded_distances_2(self):
    test_filepath = os.path.join(os.path.dirname(__file__), 'test_input.txt')
    act = get_expanded_distances(parse_input(test_filepath), 100)
    exp = 8410
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()