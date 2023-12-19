import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [[int(v) for v in line.split()] for line in get_file_lines(f)]

def predict_sequence(seq):
  if all(v == 0 for v in seq):
    return 0
  diffs = [b - a for a, b in zip(seq[:-1], seq[1:])]
  next_diff = predict_sequence(diffs)
  return seq[-1] + next_diff

def solve(input):
  return sum(predict_sequence(seq) for seq in input)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))