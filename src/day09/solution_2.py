import os
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def prepredict_sequence(seq):
  if all(v == 0 for v in seq):
    return 0
  diffs = [b - a for a, b in zip(seq[:-1], seq[1:])]
  next_diff = prepredict_sequence(diffs)
  return seq[0] - next_diff

def solve(input):
  return sum(prepredict_sequence(seq) for seq in input)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))