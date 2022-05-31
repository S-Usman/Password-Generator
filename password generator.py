#This is password generater


import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()+;:{}[]?/"
all = lower + upper + numbers + symbols
lenght = 16

password="".join(random.sample(all,lenght))
print(password)