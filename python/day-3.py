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