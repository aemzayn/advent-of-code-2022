example = '../data/example-day-1.txt'
real = '../data/day-1.txt'

with open(example, 'r') as f:
  calories = []
  current_sum = 0
  for line in f:
    if line == '\n':
      calories.append(current_sum)
      current_sum = 0
      continue
    current_sum += int(line)

  if current_sum > 0:
    calories.append(current_sum)
  
  max_calorie = max(calories)
  print(max_calorie)
   
  calories = sorted(calories)
  top_3_calories = sum(calories[-3:])
  print(top_3_calories)


