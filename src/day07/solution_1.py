import os
from collections import Counter
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

cards = 'AKQJT98765432'
card_vals = dict((v, i) for i, v in enumerate(cards[::-1]))

def parse_line(line):
  hand, bid = line.split()
  return (hand, int(bid))

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [parse_line(line) for line in get_file_lines(f)]
  
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

def score_hand(input):
  raw_hand, bid = input
  frequencies = [x[1] for x in Counter(raw_hand).most_common()]
  hand = [card_vals[v] for v in raw_hand]
  return (
    get_type(frequencies), hand, bid)

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