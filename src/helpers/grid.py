from .vector import add_vectors

def get_grid_val(grid, location):
  return grid[location[0]][location[1]]

def is_in_bounds(grid, location):
  width = len(grid)
  height = len(grid[0])
  return location[0] >= 0 and location[1] >= 0 and location[0] < width and location[1] < height

def get_neighbors(grid, location, diagonal=False):
  neighbor_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  if diagonal:
    neighbor_directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
  
  for direction in neighbor_directions:
    neighbor = add_vectors(location, direction)
    if is_in_bounds(grid, neighbor):
      yield neighbor, get_grid_val(grid, neighbor)

def iterate_grid(grid):
  for r, row in enumerate(grid):
    for c, val in enumerate(row):
      yield (r, c), val
