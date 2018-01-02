from random import *
mode = int(input("Select Mode:\n1. Basic\n2. Chaos\n"))
numPlayer = int(input("Number of players: "))
players = [""] * numPlayer
for x in range(0, numPlayer):
	players[x] = input("Player " + str(x+1) + ": ")

lowerRange = int(input("lower range: "))
upperRange = int(input("upper range: "))
print("\n")
secretInt = randint(lowerRange+1, upperRange-1)
guess = lowerRange - 1
count = -1
while (guess != secretInt):
	count = (count + 1) % numPlayer
	if (mode == 2 and count == 0):
		shuffle(players)
	print(players[count])
	guess = int(input("Choose a number between " + str(lowerRange) + " and " + str(upperRange) + ": "))
	print("\n")
	if (guess <= lowerRange or guess >= upperRange):
		print("invalid guess\n")
		count = count - 1
	elif (guess < secretInt):
		lowerRange = guess
	elif (guess > secretInt):
		upperRange = guess

print(players[count] + " got the secret number: " + str(secretInt))