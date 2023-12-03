import os
from ..helpers.math import product
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def game_product(game):
  cubes = [0,0,0]
  for pull in game['pulls']:
    if 'red' in pull:
      cubes[0] = max(cubes[0], pull['red'])
    if 'green' in pull:
      cubes[1] = max(cubes[1], pull['green'])
    if 'blue' in pull:
      cubes[2] = max(cubes[2], pull['blue'])
  return product(cubes)

def solve(input):
  return sum(game_product(game) for game in input)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))