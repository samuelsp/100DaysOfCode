from replit import clear
from art import logo
from variables import *
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

while True:  
  name = input("What is your name?: ")
  bid  = float(input("What's your bid?: $"))  
  bidders.update({name:bid})  
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  
  if more_bidders == "yes":
    clear()    
  else:
    break

def check_winner(bidders):
  highest_bid = 0
  winner = ""
  for key, value in bidders.items():
    if value > highest_bid:
      highest_bid = value
      winner = key
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    
check_winner(bidders)

  