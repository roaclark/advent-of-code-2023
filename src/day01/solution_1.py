import os
import re
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def number_from_line(line):
  first_match = re.search('^[a-z]*(\d)', line)
  last_match = re.search('(\d)[a-z]*$', line)
  if first_match is None or last_match is None:
    raise Exception(f'bad input {line}')
  return int("".join([first_match.group(1), last_match.group(1)]))

def solve(input):
  return sum([number_from_line(l) for l in input])

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))