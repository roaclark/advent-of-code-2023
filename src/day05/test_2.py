import os
import unittest
from .solution_2 import parse_input, solution, Range, get_mapped_values, map_range

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 46
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)
  
  def test_get_mapped_values_1(self):
    stable, changed = get_mapped_values(Range(55, 67), {'src': Range(50, 97), 'dest': Range(52, 99)})
    self.assertEqual(0, len(stable))
    self.assertEqual(1, len(changed))
    self.assertEqual(Range(57, 69), changed[0])

  def test_get_mapped_values_2(self):
    stable, changed = get_mapped_values(Range(74, 87), {'dest': Range(45, 67), 'src': Range(77, 99)})
    self.assertEqual(1, len(changed))
    self.assertEqual(1, len(stable))
    self.assertEqual(Range(45, 55), changed[0])
    self.assertEqual(Range(74, 76), stable[0])

  def test_map_range(self):
    mapping = [
      {'dest': Range(45, 67), 'src': Range(77, 99)},
      {'dest': Range(81, 99), 'src': Range(45, 63)},
      {'dest': Range(68, 80), 'src': Range(64, 76)},
    ]
    src = [
      Range(46, 49),
      Range(54, 62),
      Range(74, 87),
    ]
    act = sorted(map_range(src, mapping), key=lambda r: r.start)
    self.assertEqual(4, len(act))
    self.assertEqual(Range(45, 55), act[0])
    self.assertEqual(Range(78, 80), act[1])
    self.assertEqual(Range(82, 85), act[2])
    self.assertEqual(Range(90, 98), act[3])

if __name__ == '__main__':
  unittest.main()