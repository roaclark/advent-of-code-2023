import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.grid import get_neighbors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def solve(input):
  gear_numbers = {}
  for row_i in range(len(input)):
    curr_num = 0
    curr_gears = set()
    for col_i in range(len(input[row_i])):
      if input[row_i][col_i].isdigit():
        curr_num = curr_num * 10 + int(input[row_i][col_i])
        for n_loc, n_val in get_neighbors(input, (row_i, col_i), diagonal=True):
          if n_val == '*':
            curr_gears.add(n_loc)
      else:
        if curr_num:
          for gear in curr_gears:
            if gear not in gear_numbers:
              gear_numbers[gear] = []
            gear_numbers[gear].append(curr_num)
        curr_gears = set()
        curr_num = 0
    if curr_num:
      for gear in curr_gears:
        if gear not in gear_numbers:
          gear_numbers[gear] = []
        gear_numbers[gear].append(curr_num)
  res = 0
  for gear in gear_numbers:
    if len(gear_numbers[gear]) == 2:
      res += gear_numbers[gear][0] * gear_numbers[gear][1]
  return res

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))