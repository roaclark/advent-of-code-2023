import os
from ..helpers.file_parsers import get_file_lines, regex_parse_line

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  lines = []
  with open(filepath, 'r') as f:
    lines = get_file_lines(f)
  directions = lines[0]
  mapping = {}
  for l in lines[2:]:
    # AAA = (BBB, CCC)
    key, left, right = regex_parse_line(l, r"(\w+) = \((\w+), (\w+)\)")
    mapping[key] = (left, right)
  return (directions, mapping)

def solve(input):
  directions, mapping = input
  steps = 0
  pos = 'AAA'
  while pos != 'ZZZ':
    direction = directions[steps % len(directions)]
    pos = mapping[pos][0 if direction == 'L' else 1]
    steps += 1
  return steps

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))