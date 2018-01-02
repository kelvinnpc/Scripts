from random import *
numOfSides = input("Number of sides: ")
roll = True
while(roll == True):
	x = randint(1, int(numOfSides))
	print("rolled: " + str(x) + "\n")
	rollRequest = input("roll again? (y/n)")
	while(rollRequest != "y" and rollRequest != "n"):
		rollRequest = input("invalid input, y for reroll, n to terminate program\n")
	if (rollRequest == "n"):
		roll = False
print("program terminating, thanks for using :)")