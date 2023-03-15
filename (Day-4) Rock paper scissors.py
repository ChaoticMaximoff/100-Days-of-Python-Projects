import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >= 0 and user <= 2:
  print(game[user])

computer = random.randint(0, 2)
print("Computer chose:\n" + game[computer] + "\n")

# rock -> sci  0 -> 2
# sci -> pap   2 -> 1
# pap -> rock  1 -> 0
if user < 0 or user > 2:
  print("You entered an invalid number. You lose.\n")
elif user == computer:
  print("It's a draw.\n")
elif (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
  print("You win!\n")
else :
  print("You lose.\n")
  