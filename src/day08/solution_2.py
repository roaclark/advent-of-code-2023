import os
import math
from ..helpers.file_parsers import get_file_lines
from ..helpers.math import product
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  directions, mapping = input
  pos = []
  for k in mapping:
    if k[-1] == "A":
      pos.append(k)
  steps = 0
  while any(p[-1] != "Z" for p in pos):
    direction = directions[steps % len(directions)]
    pos = [mapping[p][0 if direction == 'L' else 1] for p in pos]
    steps += 1
  return steps

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))