#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo

def guess_number():
  """Returns a random number between 1 and 100"""
  return randint(1,100)

def level_difficulty():
  """Returns the number of attempts based on the difficulty level."""
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == 'easy':
    return 10
  else:
    return 5

def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def game():
  """The main game function."""
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = guess_number()
  #print(f"Pssst, the correct answer is {answer}")
  turns = level_difficulty()
  guess = 0
  attempts = []
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess not in attempts:
      turns = check_answer(guess, answer, turns)
      attempts.append(guess)
    else:
      print("You have already guessed this number.")
    if turns == 0:
      print("You've run out of guesses, you lose.") 
      print(f"The number I thought was {answer}.")
      break
    elif guess != answer:
      print("Guess again.")
  
  response = input("I would like to play again. Type 'y' or 'n': ").lower()
  if response == 'y':
    game()
  else:
     print('Bye!')
     return

if __name__ == "__main__":
  print(logo)
  game()
