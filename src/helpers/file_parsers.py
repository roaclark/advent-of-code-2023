from io import TextIOWrapper
import re

def get_file_lines(file: TextIOWrapper):
  return file.read().splitlines()

def regex_parse_line(line: str, pattern: str):
  match = re.fullmatch(pattern, line)
  if not match:
    raise Exception('Bad file parsing: ' + line + ' does not match ' + pattern)
  return match.groups()