#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = '''
____ ____ ____ ____ ____ ____ ____ ____ 
||G |||u |||e |||s |||s |||i |||n |||g ||
||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____                     
||G |||a |||m |||e ||                    
||__|||__|||__|||__||                    
|/__\|/__\|/__\|/__\|      
'''

import random

def set_difficulty_at():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  
  if difficulty == 'hard':
    return 5
  else:
   return 10
    
def start_guessing(attempts):
  won = False
  while attempts > 0 and not won:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
  
    if guess > answer:
      print("Too high.\nGuess again.")
      attempts -= 1
    elif guess < answer:
      attempts -= 1
      print("Too low.\nGuess again.")
    else:
      won = True

  return won
  
def make_game_answer():
  answer = random.randint(1, 100)
  return answer
  
def start_game(answer):
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"Pssst, the correct answer is {answer}")
  return answer



answer = make_game_answer()
start_game(answer)
attempts = set_difficulty_at()
game_won = start_guessing(attempts)

if game_won:
  print(f"You got it! The answer was {answer}")
else:
  print("You've run out of guesses, you lose.")