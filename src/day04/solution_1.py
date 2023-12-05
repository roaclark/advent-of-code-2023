import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  lines = []
  with open(filepath, 'r') as f:
    for line in get_file_lines(f):
      _, values = line.split(':')
      winning, have = values.split('|')
      lines.append(([int(v) for v in winning.split()], [int(v) for v in have.split()]))
  return lines

def solve(input):
  res = 0
  for card in input:
      overlaps = len(set(card[0]).intersection(set(card[1])))
      if overlaps:
        res += pow(2, overlaps - 1)
  return res

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))