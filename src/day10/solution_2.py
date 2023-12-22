import os
from .solution_1 import parse_input, get_pipe_neighbors, get_start_location, get_next_pipe, get_start_neighbors
from ..helpers.grid import is_in_bounds, iterate_grid, get_neighbors, get_grid_val
from ..helpers.vector import add_vectors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# def get_pipe_neighbors(grid, loc, typ):
# def get_start_location(grid):
# def get_next_pipe(grid, prev, curr):

def get_loop(grid):
  start = get_start_location(grid)
  loop = [start]
  prev = start
  curr = get_start_neighbors(grid, start)[0]
  while curr != start:
    loop.append(curr)
    prev, curr = curr, get_next_pipe(grid, prev, curr)
  return loop

def extend_loop(loop):
  new_loop = []
  for i in range(len(loop) - 1):
    new_loop.append(add_vectors(loop[i], loop[i]))
    new_loop.append(add_vectors(loop[i], loop[i+1]))
  new_loop.append(add_vectors(loop[-1], loop[-1]))
  new_loop.append(add_vectors(loop[-1], loop[0]))
  return new_loop

def solve(grid):
  height = len(grid)
  width = len(grid[0])
  loop = get_loop(grid)
  extendo_grid = [[False for _ in range(width * 2)] for _ in range(height * 2)]
  search_queue = [(0, x) for x in range(width * 2)] + [(height * 2 - 1, x) for x in range(width * 2)] + [(x, 0) for x in range(1, height * 2 - 1)] + [(x, width * 2 - 1) for x in range(1, height * 2 - 1)]
  outside_set = set(extend_loop(loop))
  while search_queue: 
    curr = search_queue.pop()
    if curr not in outside_set:
      outside_set.add(curr)
      for n, _v in get_neighbors(extendo_grid, curr):
        search_queue.append(n)
  cnt_outside = sum(1 for x in outside_set if x[0] % 2 == 0 and x[1] % 2 == 0)
  return height * width - cnt_outside

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))