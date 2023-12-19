import os
from collections import namedtuple
from .solution_1 import solve
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
Range = namedtuple('Range', ['start', 'end'])

def parse_input(filepath):
  seeds = None
  mappings = []
  with open(filepath, 'r') as f:
    for line in get_file_lines(f):
      if seeds is None:
        seeds = []
        seed_configs = [int(x) for x in line[7:].split(" ")]
        for i in range(0, len(seed_configs), 2):
          seeds.append(Range(seed_configs[i], seed_configs[i] + seed_configs[i+1] - 1))
      else:
        if len(line) != 0:
          if line.endswith("map:"):
            mappings.append([])
          else:
            dest_start, src_start, length = [int(x) for x in line.split(" ")]
            mappings[-1].append({
              'dest': Range(dest_start, dest_start + length - 1),
              'src': Range(src_start, src_start + length - 1),
            })
  return {
    'seeds': seeds,
    'mappings': mappings,
  }

def get_mapped_values(src, mapping):
  # src: Range
  # mapping: Range
  map_start = mapping['src'].start
  map_end = mapping['src'].end
  
  stable = []
  changed = []

  if map_start > src.start:
    stable.append(Range(src.start, min(src.end, map_start - 1)))
  if map_end < src.end:
    stable.append(Range(max(map_end + 1, src.start), src.end))
  
  overlap_start = max(map_start, src.start)
  overlap_end = min(map_end, src.end)
  if overlap_start <= overlap_end:
    diff = mapping['dest'].start - mapping['src'].start
    changed.append(Range(overlap_start + diff, overlap_end + diff))
  return (stable, changed)

def map_range(src, mapping):
  # src: Range[]
  # mapping: {dest: Range, src: Range}[]
  # return: Range[]
  mapped_values = []
  curr_src = src
  for map_rng in mapping:
    new_src = []
    for src_rng in curr_src:
      stable, changed = get_mapped_values(src_rng, map_rng)
      mapped_values += changed
      new_src += stable
    curr_src = new_src
  return mapped_values + curr_src

def solve(input):
  curr_range = input['seeds']
  mappings = input['mappings']
  for mapping in mappings:
    curr_range = map_range(curr_range, mapping)
  return min(r.start for r in curr_range)
  

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))