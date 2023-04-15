import random
import art
from game_data import data
from replit import clear
  

def display_game_data(choice_a, choice_b):
  """formats and displays data of each round"""
  a_an_a = 'a'
  a_an_b = 'a'
  
  if choice_a['description'][0].lower() == 'a':
    a_an_a = 'an'

  if choice_b['description'][0].lower() == 'a':
    a_an_b = 'an'
  
  print(f"Compare A: {choice_a['name']}, {a_an_a} {choice_a['description']}, from {choice_a['country']}.")
  print(art.vs)
  print(f"Against B: {choice_b['name']}, {a_an_b} {choice_b['description']}, from {choice_b['country']}.")


game_over = False
score = 0
choice_a = random.choice(data)
choice_b = random.choice([i for i in data if i != choice_a])

while not game_over:
  print(art.logo)
  
  if score > 0:
    print(f"You're right! Current score: {score}.")
  
  if choice_a['follower_count'] > choice_b['follower_count']:
    answer = 'a'
  else:
    answer = 'b'

  display_game_data(choice_a, choice_b)

  user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

  if user_input == answer:
    score += 1
    choice_a = choice_b
    choice_b = random.choice([i for i in data if i != choice_a])

  else:
    game_over = True

  clear()

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")

    