import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	line = inputFile.readline()

for char in range(len(line)):
	upCount = line[:char].count("(")
	downCount = line[:char].count(")")
	finalFloor = upCount - downCount
	if(finalFloor == -1):
		print(char)
		break
