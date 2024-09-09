import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	boxDimensions = [line[:-1] for line in inputFile]

def main():
	totalLength = 0

	for box in boxDimensions:
		dimensions = [int(dimension) for dimension in box.split("x")]

		length = dimensions[0]
		width = dimensions[1]
		height = dimensions[2]

		ribbonLength = 2 * (sum(dimensions) - max(dimensions))
		bowLength = length * width * height

		totalLength += ribbonLength + bowLength

	return totalLength
