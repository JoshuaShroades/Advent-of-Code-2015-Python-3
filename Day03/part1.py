import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	line = inputFile.readline()

def main():
	xPos = 0
	yPos = 0
	visitedCoordinates = {(0,0)}

	for char in line:
		match char:
			case "^":
				xPos += 1
			case "v":
				xPos -= 1
			case ">":
				yPos += 1
			case "<":
				yPos -= 1
		visitedCoordinates.add((xPos, yPos))

	return len(visitedCoordinates)