from art import logo
from alphabet import alphabet
def caesar_cipher(plain_text, shift_amount, cipher_direction):
  def encrypt(text, shift):
    cipher_text = ''
    for char in text:
      capital = False
      if char.isupper():
        capital = True
      char = char.lower()
      if char in alphabet:
        position = alphabet.index(char) + shift
        if position > number_of_letters:
          position = position - number_of_letters - 1
        if capital:
          cipher_text += alphabet[position].upper()
        else:
          cipher_text += alphabet[position]
      else:
        cipher_text += char
    return f"The encoded text is {cipher_text}."

  def decrypt(cipher_text, shift):
    decoded_text = ''
    for char in cipher_text:
      capital = False
      if char.isupper():
        capital = True
      char = char.lower()
      if char in alphabet:
        position = alphabet.index(char) - shift
        if position < 0:
          position = number_of_letters - abs(position) + 1
        if capital:
          decoded_text += alphabet[position].upper()
        else:
          decoded_text += alphabet[position]
      else:
        decoded_text += char
    return f"The decoded text is {decoded_text}."

  number_of_letters = len(alphabet) - 1
  shift_amount = shift_amount % number_of_letters

  if cipher_direction == 'encode':
    return encrypt(text=plain_text, shift=shift_amount)
  elif cipher_direction == 'decode':
    return decrypt(cipher_text=plain_text, shift=shift_amount)
  else:
    return "Invalid option!"

print(logo)
again = 'yes'
while again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    print(caesar_cipher(plain_text=text, shift_amount=shift, cipher_direction=direction))
    while again != 'no':
      again = input("Type 'yes' if you want to go again.Otherwise type 'no'. ").lower()
      if again == 'no':
        print("Goodbye!")
        break
      elif again == 'yes':
        break
      else:
        print("Invalid option! Try again.")
        continue

