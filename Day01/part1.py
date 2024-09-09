import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	line = inputFile.readline()

def main():
	upCount = line.count("(")
	downCount = line.count(")")
	finalFloor = upCount - downCount

	return finalFloor
