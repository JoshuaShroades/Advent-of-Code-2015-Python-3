import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input1.txt")

with open(inputFilePath) as inputFile:
	line = inputFile.readline()
	upCount = line.count("(")
	downCount = line.count(")")
	finalFloor = upCount - downCount
	print(finalFloor)
