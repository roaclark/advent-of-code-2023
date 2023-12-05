import os
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  res = 0
  adds = []
  for card in input:
    count = 1
    if adds:
      count += adds.pop(0)
    overlaps = len(set(card[0]).intersection(set(card[1])))
    for _ in range(overlaps - len(adds)):
      adds.append(0)
    for i in range(overlaps):
      adds[i] += count
    res += count
  return res

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))