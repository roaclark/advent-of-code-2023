import os
from .solution_1 import parse_input, get_expanded_distances

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(grid):
  return get_expanded_distances(grid, 1000000)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))