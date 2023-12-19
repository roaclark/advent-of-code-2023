import os
from ..helpers.file_parsers import get_file_lines
from .solution_1 import solve

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    time_str, dist_str = get_file_lines(f)
    time = int(''.join(time_str.split()[1:]))
    dist = int(''.join(dist_str.split()[1:]))
    return [(time, dist)]

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))