import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  seeds = None
  mappings = []
  # seed-to-soil
  # soil-to-fertilizer
  # fertilizer-to-water
  # water-to-light
  # light-to-temperature
  # temperature-to-humidity
  # humidity-to-location
  with open(filepath, 'r') as f:
    for line in get_file_lines(f):
      if seeds is None:
        seeds = [int(x) for x in line[7:].split(" ")]
      else:
        if len(line) != 0:
          if line.endswith("map:"):
            mappings.append([])
          else:
            dest_start, src_start, length = [int(x) for x in line.split(" ")]
            mappings[-1].append({
              'dest_start': dest_start,
              'src_start': src_start,
              'length': length,
            })
  return {
    'seeds': seeds,
    'mappings': mappings,
  }

def pass_through_mapping(src, mapping):
  mapping = sorted(mapping, key=lambda x: x['src_start'])
  map_i = -1
  while map_i < len(mapping) - 1 and mapping[map_i + 1]['src_start'] <= src:
    map_i += 1
  if map_i == -1:
    return src
  mapping_range = mapping[map_i]
  if src < mapping_range['src_start'] + mapping_range['length']:
    return src - mapping_range['src_start'] + mapping_range['dest_start']
  return src

def pass_through_all_mappings(src, mappings):
  curr = src
  for mapping in mappings:
    curr = pass_through_mapping(curr, mapping)
  return curr

def solve(input):
  return min(pass_through_all_mappings(seed, input['mappings']) for seed in input['seeds'])

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))