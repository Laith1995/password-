letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

first=[]
for a in range(1,nr_letters+1):
   l = random.choice(letters)
   first+=l


for b in range (1,nr_numbers+1):
    n = random.choice(numbers)
    first+=n


for c in range(1,nr_symbols+1):
    s = random.choice(symbols)
    first+=s


random.shuffle(first)
final_password=""
for d in first :
    final_password+=d

print(f"Your new password is : {final_password}")




#final_password= ''.join(final2)
#print(final_password)