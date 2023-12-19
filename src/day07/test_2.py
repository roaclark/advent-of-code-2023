import os
import unittest
from .solution_2 import solution, get_hand_type

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 5905
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)
  
  def test_get_hand_type(self):
    # 6 = Five of a kind
    # 5 = Four of a kind
    # 4 = Full house
    # 3 = Three of a kind
    # 2 = Two pair
    # 1 = One pair
    # 0 = High card
    self.assertEqual(1, get_hand_type('32T3K'))
    self.assertEqual(5, get_hand_type('T55J5'))
    self.assertEqual(2, get_hand_type('KK677'))
    self.assertEqual(5, get_hand_type('KTJJT'))
    self.assertEqual(5, get_hand_type('QQQJA'))
    self.assertEqual(6, get_hand_type('JJJJJ'))

if __name__ == '__main__':
  unittest.main()