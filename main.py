#Password Generator Project

# Importing random module
import random

# Predefined variables to decrease repetation

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Error handling and input storing

print("Welcome to the PyPassword Generator!")
try:
 nr_letters= int(input("How many letters would you like in your password?\n"))
 nr_symbols = int(input(f"How many symbols would you like?\n"))
 nr_numbers = int(input(f"How many numbers would you like?\n"))
except ValueError:
    print("That's not a valid number!")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Defining lists for later use

letters1 = []
numbers1 = []
symbols1 = []

# Error handling and password generation

try:
 if nr_letters and nr_numbers and nr_symbols:
#  Generation of letters
  for x in range(nr_letters):
     randc = random.randint(0,51)
     letters1.append(letters[randc])
     
# Generation of numbers
  for x in range(nr_numbers):
     randn = random.randint(0,8)
     numbers1.append(numbers[randn])

# Generation of symbols
  for x in range(nr_symbols):
     rands = random.randint(0,8)
     symbols1.append(symbols[rands])
 else:
   print("Any value cant be 0, please try again.")
   
# Shuffling for protection

 password = letters1 + numbers1 + symbols1
 passshufle = random.shuffle(password)
 print("Your password is : ")
 print(''.join(password))
except NameError:
    print("Please try again.")

# Preventing auto exit

input("Press enter to exit.")
