from random import *

allChar = ["!","@","#", "$", "%", "^", "&", "*","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
passLength = int(input("How long would you like your password to be? >> "))

password = []

for x in range(passLength):
    password.append(allChar[randint(0,len(allChar))])
    
print("Your new password is: " + "".join(password))
