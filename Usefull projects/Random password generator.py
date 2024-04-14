import random
chars = "abcdefghijklmnopqrstuvxyz1234567890!@#$&\?8ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = int(input("Enter length of the password: "))
password= ""

for a in range (length):
   password+= random.choice (chars)
print(password)