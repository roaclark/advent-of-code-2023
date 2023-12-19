import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.math import product

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    times_str, dist_str = get_file_lines(f)
    times = [int(x) for x in times_str.split()[1:]]
    dists = [int(x) for x in dist_str.split()[1:]]
    return zip(times, dists)

def win_ways(time, dist):
  charge_time = 0
  while charge_time * (time - charge_time) <= dist and charge_time <= time // 2:
    charge_time += 1
  return time + 1 - charge_time * 2

def solve(input):
  return product([win_ways(t, d) for t, d in input])

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))