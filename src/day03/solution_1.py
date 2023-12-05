import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.grid import get_neighbors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def solve(input):
  res = 0
  for row_i in range(len(input)):
    curr_num = 0
    curr_valid = False
    for col_i in range(len(input[row_i])):
      if input[row_i][col_i].isdigit():
        curr_num = curr_num * 10 + int(input[row_i][col_i])
        if not curr_valid:
          for _n, val in get_neighbors(input, (row_i, col_i), diagonal=True):
            if not val.isdigit() and val != '.':
              curr_valid = True
      else:
        if curr_valid and curr_num:
          res += curr_num
        curr_valid = False
        curr_num = 0
    if curr_valid and curr_num:
      res += curr_num
  return res

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))