import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	boxDimensions = [line[:-1] for line in inputFile]

totalArea = 0

for box in boxDimensions:
	dimensions = [int(dimension) for dimension in box.split("x")]

	length = dimensions[0]
	width = dimensions[1]
	height = dimensions[2]

	surfaceArea = 2 * (length * width + length * height + width * height)
	slack = int(length * width * height / max(dimensions))

	totalArea += surfaceArea + slack

print(totalArea)
