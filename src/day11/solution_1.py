import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.grid import iterate_grid
from ..helpers.vector import add_vectors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def get_expanded_distances(grid, expansion=2):
  galaxies = []
  for loc, val in iterate_grid(grid):
    if val == "#":
      galaxies.append(loc)

  galaxies.sort(key=lambda x: x[0])
  v_expanded = [galaxies[0]]
  v_spread = 0
  for i in range(1, len(galaxies)):
    gaps = max(0, galaxies[i][0] - galaxies[i-1][0] - 1)
    v_spread += gaps * (expansion - 1)
    v_expanded.append(add_vectors(galaxies[i], (v_spread, 0)))
  galaxies = v_expanded

  galaxies.sort(key=lambda x: x[1])
  h_expanded = [galaxies[0]]
  h_spread = 0
  for i in range(1, len(galaxies)):
    gaps = max(0, galaxies[i][1] - galaxies[i-1][1] - 1)
    h_spread += gaps * (expansion - 1)
    h_expanded.append(add_vectors(galaxies[i], (0, h_spread)))
  galaxies = h_expanded

  tot_dist = 0
  for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
      tot_dist += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
  return tot_dist

def solve(grid):
  return get_expanded_distances(grid, 2)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))