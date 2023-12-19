import os
from collections import Counter
from ..helpers.file_parsers import get_file_lines
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
cards = 'AKQT98765432J'
card_vals = dict((v, i) for i, v in enumerate(cards[::-1]))

def get_type(frequencies):
  if frequencies[0] == 5:
    return 6
  if frequencies[0] == 4:
    return 5
  if frequencies[0] == 3:
    return 4 if frequencies[1] == 2 else 3
  if frequencies[0] == 2:
    return 2 if frequencies[1] == 2 else 1
  return 0

def get_hand_type(hand):
  card_frequencies = Counter(hand)
  jokers = card_frequencies['J']
  del card_frequencies['J']
  frequencies = [x[1] for x in card_frequencies.most_common()]
  if len(frequencies) > 0:
    frequencies[0] += jokers
  else:
    frequencies.append(jokers)
  return get_type(frequencies)

def score_hand(input):
  raw_hand, bid = input
  hand = [card_vals[v] for v in raw_hand]
  return (get_hand_type(raw_hand), hand, bid)

def solve(input):
  hands = sorted(score_hand(x) for x in input)
  score = 0
  for i, value in enumerate(hands):
    score += (i + 1) * value[2]
  return score

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))