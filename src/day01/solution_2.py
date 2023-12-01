import os
import re
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

digit_map = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def digit_from_string(s):
  if s in digit_map:
    return digit_map[s]
  return s

def number_from_line(line):
  digit_match_text = '|'.join(digit_map.keys())
  matches = re.findall(f'(?=(\d|{digit_match_text}))', line)
  if len(matches) < 1:
    raise Exception(f'bad input {line}')
  return int("".join([digit_from_string(matches[0]), digit_from_string(matches[-1])]))

def solve(input):
  return sum([number_from_line(l) for l in input])

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))