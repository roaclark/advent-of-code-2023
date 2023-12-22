import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.vector import add_vectors
from ..helpers.grid import is_in_bounds, iterate_grid, get_neighbors, get_grid_val

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

pipe_neighbors = {
  '|': [(-1, 0), (1, 0)],
  '-': [(0, -1), (0, 1)],
  'F': [(1, 0), (0, 1)],
  'J': [(-1, 0), (0, -1)],
  '7': [(1, 0), (0, -1)],
  'L': [(-1, 0), (0, 1)],
  '.': [],
}

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def get_start_location(grid):
  for pos, v in iterate_grid(grid):
    if v == 'S':
      return pos
  raise Exception('No start position found')

def get_start_neighbors(grid, start):
  neighbors = []
  for n, v in get_neighbors(grid, start):
    for n_n in get_pipe_neighbors(grid, n, get_grid_val(grid, n)):
      if n_n == start:
        neighbors.append(n)
  if len(neighbors) != 2:
    raise Exception('Expected exactly two start neighbors; neighbors: ' + str(curr_pos))
  return neighbors

def get_pipe_neighbors(grid, loc, typ):
  for d in pipe_neighbors[typ]:
    n = add_vectors(loc, d)
    if is_in_bounds(grid, n):
      yield n

def get_next_pipe(grid, prev, curr):
  neighbors = get_pipe_neighbors(grid, curr, get_grid_val(grid, curr))
  for n in neighbors:
    if n != prev:
      return n
  raise Exception('No next pipe found; location: ' + str(curr))

def solve(grid):
  start = get_start_location(grid)
  prev_pos = [start, start]
  curr_pos = get_start_neighbors(grid, start)
  if len(curr_pos) != 2:
    raise Exception('Expected exactly two start neighbors; neighbors: ' + str(curr_pos))
  curr_steps = 1
  while curr_pos[0] != curr_pos[1]:
    next_0 = get_next_pipe(grid, prev_pos[0], curr_pos[0])
    next_1 = get_next_pipe(grid, prev_pos[1], curr_pos[1])
    prev_pos = curr_pos
    curr_pos = [next_0, next_1]
    curr_steps += 1
  return curr_steps

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))