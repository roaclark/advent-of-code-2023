import os
import unittest
from .solution_1 import parse_input, solution

class TestSolution(unittest.TestCase):
  def test_parse_input(self):
    act = parse_input(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual([79, 14, 55, 13], act['seeds'])
    self.assertEqual(7, len(act['mappings']))
    self.assertEqual({
      'dest_start': 50,
      'src_start': 98,
      'length': 2,
    }, act['mappings'][0][0])

  def test_solution(self):
    exp = 35
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()