import os
import re
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_game(line):
  game_string, pulls_string = line.split(":")
  game_num = int(game_string.split(' ')[1])
  game_data = {'id': game_num, 'pulls': []}
  pulls = pulls_string.split(';')
  for pull in pulls:
    pull_data = {}
    matches = re.findall('\w+', pull)
    for i in range(0, len(matches), 2):
      pull_data[matches[i+1]] = int(matches[i])
    game_data['pulls'].append(pull_data)
  return game_data

def parse_input(filepath):
  games = []
  with open(filepath, 'r') as f:
    for line in get_file_lines(f):
      games.append(parse_game(line))
  return games

def solve(input):
  res = 0
  for game in input:
    valid = True
    for pulls in game['pulls']:
      if 'red' in pulls and pulls['red'] > 12:
        valid = False
      if 'green' in pulls and pulls['green'] > 13:
        valid = False
      if 'blue' in pulls and pulls['blue'] > 14:
        valid = False
    if valid:
      res += game['id']
  return res


def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))