target = input("Targeted file: ")
f = open(target, 'r')
file = f.read()
f.close()

count = 0
o = open('output.txt', 'a')
for char in file:
	if(char != '\n'):
		o.write(char)
		count = count + 1
	if (count == 64):
		o.write('\n')
		count = 0

