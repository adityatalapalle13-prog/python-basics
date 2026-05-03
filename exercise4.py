import string
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.ascii_letters)

word=input("Enter the word: ")
if len(word)<3:
