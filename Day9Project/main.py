from art import logo
from variables import *
from time import sleep

print(logo)
print("Welcome to the secret auction program.")

while True:
  sleep(3)
  name = input("What is your name?: ")
  bid  = int(input("What's your bid?: $"))  
  bidders.update({name:bid})  
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  
  if more_bidders == "yes":
    continue
  else:
    break

for key, value in bidders.items():
  if value > max_value:
    max_value = value
    winner = key

print(f"The winner is {winner} with a bid of ${max_value}")
  