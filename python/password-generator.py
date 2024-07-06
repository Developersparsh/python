import random
chars="1234567890-=!@#$%^&*()_+qwertyuiop[]\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?"
length=int(input("enter length:"))
password=""

for a in range(length):
  password+=random.choice(chars)
print(password)