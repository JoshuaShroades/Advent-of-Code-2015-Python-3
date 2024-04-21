import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	line = inputFile.readline()

xPos = [0, 0]
yPos = [0, 0]
visitedCoordinates = {(0,0)}
robot = 0

for char in line:
	match char:
		case "^":
			xPos[robot] += 1
		case "v":
			xPos[robot] -= 1
		case ">":
			yPos[robot] += 1
		case "<":
			yPos[robot] -= 1
	visitedCoordinates.add((xPos[robot], yPos[robot]))
	robot = (robot + 1) % 2

print(len(visitedCoordinates))
