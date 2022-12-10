example = './example.txt'
real = './input.txt'

def split_sections(line):
  sections = line.split(',')
  return [list(map(lambda i: int(i), section.split('-'))) for section in sections]

def fully_overlaps(sections):
  task1, task2 = sections[0], sections[1]
  if task1[0] <= task2[0] and task1[1] >= task2[1]:
    return True
  return False

def overlaps(sections):
  t1, t2 = sections[0], sections[1]
  return (t1[0] <= t2[1] and t1[1] >= t2[0]) or (t2[0] <= t1[0] and t2[0] >= t1[1])  

def check_in_range(x, range):
  return x >= range[0] and x <= range[1]

with open(real, 'r') as f:
  total_full_overlaps = 0
  for line in f:
    line = line.strip()
    sections = split_sections(line)
    has_overlap = fully_overlaps(sections)
    if has_overlap:
      total_full_overlaps += 1
  # print(f"#1 fully overlapping tasks {total_full_overlaps}")

with open(real, 'r') as f:
  total_overlaps = 0
  for line in f:
    line = line.strip()
    sections = split_sections(line)
    has_overlap = overlaps(sections)
    if has_overlap:
      print(has_overlap, sections)
      total_overlaps += 1
  print(f"#2 overlaps task {total_overlaps}")