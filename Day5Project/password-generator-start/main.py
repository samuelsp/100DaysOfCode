#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '-']

splash = '''
  ____  _____  ____   _____   ____  _____  _| |_  _____   
 / _  || ___ ||  _ \ | ___ | / ___)(____ |(_   _)| ___ |  
( (_| || ____|| | | || ____|| |    / ___ |  | |_ | ____|  
 \___ ||_____)|_| |_||_____)|_|    \_____|   \__)|_____)  
(_____|                                                   
                                                    _ 
                                                   | |
 ____   _____   ___   ___  _ _ _   ___    ____   __| |
|  _ \ (____ | /___) /___)| | | | / _ \  / ___) / _  |
| |_| |/ ___ ||___ ||___ || | | || |_| || |    ( (_| |
|  __/ \_____|(___/ (___/  \___/  \___/ |_|     \____|
|_|                            

'''

print("Welcome to the PyPassword Generator!")
print(splash)

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letters = random.sample(letters, nr_letters)
random_numbers = random.sample(numbers, nr_numbers)
random_symblos = random.sample(symbols, nr_symbols)

password = random_letters + random_numbers + random_symblos
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
password_randomized = "".join(password)
print(f"Your password is: {password_randomized}")


