import os

stages = [("\n"),
("------\n"),
("------\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"),
("------\n"
"|  |\n"
"|\n"
"|\n"
"|\n"
"|\n"),
("------\n"
"|  |\n"
"|  O\n"
"|\n"
"|\n"
"|\n"),
("------\n"
"|  |\n"
"|  O\n"
"|  |\n"
"|\n"
"|\n"),
("------\n"
"|  |\n"
"|  O\n"
"| /|\n"
"|\n"
"|\n"),
("------\n"
"|  |\n"
"|  O\n"
"| /|\\\n"
"|\n"
"|\n"),
("------\n"
"|  |\n"
"|  O\n"
"| /|\\\n"
"|  /\n"
"|\n"),
("------\n"
"|  |\n"
"|  O\n"
"| /|\\\n"
"|  /\\\n"
"|\n")]

# for x in stages:
# 	print(x)

word = input("Key in the word to guess: ")
string = []
for x in range(0,len(word)):
	string.append("_")

os.system('cls')
numTry = int(input("number of guesses: "))

count = 0
guessed = []
while (count < numTry):
	guess = input("Guess an alphabet: ")
	if guess not in guessed:
		guessed.append(guess)
		if guess not in word:
			count = count + 1

	index = 0
	while guess in word[index:]:
		index = word.index(guess, index) + 1
		string[index - 1] = guess
	
	print(stages[count * 9 // numTry])
	print(string)
	print("Number of error left: " + str(numTry - count))
