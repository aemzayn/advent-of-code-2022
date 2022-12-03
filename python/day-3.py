example = '../data/example-day-3.txt'
real = '../data/day-3.txt'

def find_same_item(first_compartment, second_compartment):
  for item in first_compartment:
    if item in second_compartment:
      return item

def get_priority(item):
  if item.lower() == item:
    return ord(item) - 96
  return ord(item) - 38

# part one
with open(real, 'r') as f:
  priorities = []
  for line in f:
    line = line.strip()
    mid = len(line)//2
    first_compartment, second_compartment = line[:mid], line[mid:]
    same_item = find_same_item(first_compartment, second_compartment)
    priorities.append(get_priority(same_item))
  sum_of_priorities = sum(priorities)
  print(f"Sum of priorities: {sum_of_priorities}")

# part two
def find_group_common(groups):
  commons = []
  for _, group in  groups.items():
    sorted_group = sorted(group, key=lambda x: len(x))
    shortest_item = sorted_group[0]
    for c in shortest_item:
      if c in sorted_group[1] and c in sorted_group[2]:
        commons.append(get_priority(c))
        break
  return commons

with open(real, 'r') as f:
  current_group = []
  group_index = 0
  groups = {}
  for i, line in enumerate(f):
    line = line.strip()
    if i % 3 == 0:
      group_index += 1
    if group_index in groups:
      groups[group_index].append(line)
    else:
      groups[group_index] = [line]

  commons = find_group_common(groups)
  sum_of_commons = sum(commons)
  print(f"Sum of common priorities: {sum_of_commons}")