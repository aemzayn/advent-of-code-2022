example = '../data/example-day-2.txt'
real = '../data/day-2.txt'

WIN_SCORE = 6
DRAW_SCORE = 3
LOST_SCORE = 0
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

strategies = {
  rock: {
    'win': scissors,
    'lost': paper,
    'score': 1
  },
  paper: {
    'win': rock,
    'lost': scissors,
    'score': 2
  },
  scissors: {
    'win': paper,
    'lost': rock,
    'score': 3
  },
}

choices_map = {
  'A': rock,
  'B': paper,
  'C': scissors,
  'X': rock,
  'Y': paper,
  'Z': scissors,
}


def check_winner(player_choice, opponent_choice):
  score = strategies[player_choice]['score']
  if strategies[player_choice]['win'] == opponent_choice:
    # player win
    return score + WIN_SCORE
  elif strategies[player_choice]['lost'] == opponent_choice:
    # player lost
    return score + LOST_SCORE
  else:
    # draw
    return score + DRAW_SCORE 

def part_one(lines):
  total_score = 0
  for line in lines:
    opponent, player = line[0], line[2]
    score = check_winner(
      choices_map[player],
      choices_map[opponent],
    )
    total_score += score
    # print(score)
  print(f'Total score: {total_score}')

def make_choice(player_strategy, opponent_choice):
  opponent_strategy = strategies[opponent_choice]

  if player_strategy == 'X':
    # player should lost
    player_choice = opponent_strategy['win']
    return strategies[player_choice]['score'] + LOST_SCORE
  elif player_strategy == 'Y':
    # player should draw
    return opponent_strategy['score'] + DRAW_SCORE
  else:
    # player should win
    player_choice = opponent_strategy['lost']
    return strategies[player_choice]['score'] + WIN_SCORE
  

def part_two(lines):
  total_score = 0
  for line in lines:
    opponent, player = line[0], line[2]
    score = make_choice(player, choices_map[opponent])
    total_score += score
  print(f'Total score: {total_score}')

# with open(real, 'r') as f:
#   part_one(f)

with open(real, 'r') as f:
  part_two(f)