from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
cont = True
win_bid = 0
win_name = ""
while cont:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  if bid > win_bid:
    win_bid = bid
    win_name = name
  answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if answer == "yes":
    clear()
  else:
    cont = False
clear()
print(f"The winner is {win_name} with a bid of ${bidders[win_name]}.\n")