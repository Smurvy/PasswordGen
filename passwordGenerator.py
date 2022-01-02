from random import *

specialChar = ["!","@","#", "$", "%", "^", "&", "*",]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

passLength = int(input("How long would you like your password to be? >> "))

password = []

for x in range(passLength):
    typeChoice = randint(1,3)

    if typeChoice == 1:
        password.append(specialChar[randint(0,len(specialChar) + 1)])

    elif typeChoice == 2:
        password.append(alphabet[randint(0,len(alphabet) + 1)])

    elif typeChoice == 3:
        password.append(num[randint(0,len(num) + 1)])

print("Your new password is: " + "".join(password))