from random import *

lowerRange = int(input("lower range: "))
upperRange = int(input("upper range: "))
secretInt = randint(lowerRange+1, upperRange-1)
guess = lowerRange - 1

while (guess != secretInt):
	guess = int(input("Choose a number between " + str(lowerRange) + " and " + str(upperRange) + ": "))
	if (guess <= lowerRange or guess >= upperRange):
		print("invalid guess\n")
	elif (guess < secretInt):
		lowerRange = guess
	elif (guess > secretInt):
		upperRange = guess

print("You got the secret number: " + str(secretInt))