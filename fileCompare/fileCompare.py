import sys

targetFile = input("Target file: ")
referenceFile = input("Reference file: ")

fTarget = open(targetFile, "r")
target = fTarget.read()
fTarget.close()
fReference = open(referenceFile, "r")
reference = fReference.read()
fReference.close()
# target = target.replace("\\r\\n", "\\n")
# target = target.replace("\\r", "\\n")
# reference = reference.replace("\\r\\n", "\\n")
# reference = reference.replace("\\r", "\\n")
line = 1
for i in range(len(reference)):
	if(target[i] != reference[i]):
		print("line:" + str(line) + " is not the same")
		print(target[i] + " " + reference[i])
		sys.exit()
	elif(reference[i] == "\n"):
		line = line + 1

print("The two files are the same")