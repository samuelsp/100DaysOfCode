from random import choice
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
guessed_letters = []

def chosen_word():
  return choice(word_list)

word = chosen_word()
display = ["_" for _ in range(len(word))]

def play_won():
  if "_" not in display:
    return True
  return False

def play_lost():
  if lives == 0:
    return True
  return False

def show_display():
  print(stages[lives])
  print(" ".join(display))
  print("\n")

def game_over():
  if play_won():
    print("\nYou win.")
    return True
  if play_lost():
    print("\nYou lose.")
    return True
  return False
  
print(logo)
print(f'Pssst, the solution is {word}.')
end_of_game = False
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
while not end_of_game:
  show_display()  
  guess = input("Guess a letter: ").lower()  

  if guess in guessed_letters:
    print("You already guessed this letter. Try again.")
    continue  

  if not guess.isalpha():
    print("Invalid input. Please enter a letter.")
    continue

#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  for index, letter in enumerate(word):
    if letter == guess:
        display[index] = letter   

  if guess not in word:
    lives -= 1
    
  end_of_game = game_over()
  
  if end_of_game:  
    show_display()
    print(f"The word was {word}.")
  else:
    guessed_letters.append(guess)
      

