example = '../data/example-day-4.txt'
real = '../data/day-4.txt'

def split_sections(line):
  sections = line.split(',')
  return [list(map(lambda i: int(i), section.split('-'))) for section in sections]

def section_check(sections):
  task1, task2 = sections[0], sections[1]
  if is_contains(task1, task2) or is_contains(task2, task1):
    return True
  return False

def is_contains(task1, task2):
  if task1[0] <= task2[0] and task1[1] >= task2[1]:
    return True
  return False 

with open(real, 'r') as f:
  overlapped_task = 0
  for line in f:
    line = line.strip()
    sections = split_sections(line)
    has_overlap = section_check(sections)
    if has_overlap:
      overlapped_task += 1

  print(f"total overlapped task {overlapped_task}")