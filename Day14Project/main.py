from random import choice

from art import logo, vs
from game_data import data


def choose_personality():
  """
  Chooses a random personality from the data list.
  """
  return choice(data) 

def show_data_personality(personality):
  """
  Returns a string representing a personality's name, description, and country.
  """
  name        = personality['name']
  description = personality['description']
  country     = personality['country']
  return f"{name}, a {description}, from {country}"

def compare_followers(personality_a, personality_b):
  """
  Compares the followers of the two personality and returns the one with the 
  highest followers.
  """
  if personality_a > personality_b:
    return 'A'
  return 'B'
  
def game():
  """
  The main game function.
  """
  play_game, score = True, 0
  personality_a = choose_personality()
  personality_b = choose_personality()

  while play_game:

    while personality_a == personality_b:
      personality_a = choose_personality()
    
    followers_a = personality_a['follower_count']
    followers_b = personality_b['follower_count']

    print(f"Compare A: {show_data_personality(personality_a)}.")
    print(vs)
    print(f"Against B: {show_data_personality(personality_b)}.")

    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if player_choice == compare_followers(followers_a, followers_b):
      score += 1

      print(f"You're right! Current score: {score}.")
      print("")

      if player_choice == 'B':
        personality_a = personality_b

      personality_b = choose_personality()

    else:
      print(f"Sorry, that's wrong. Final score: {score}.")
      print(f"{personality_a['name']}, followers: {followers_a} millions.")
      print(f"{personality_b['name']}, followers: {followers_b} millions.")
      print("")
      play_game = False
    
  continue_game = input("Do you want to continue type 'Y' or 'N' for no? ").upper()

  if continue_game == 'N':
    print('Bye!')
    return
  return game()
  
if __name__ == "__main__":
  print(logo)
  game()