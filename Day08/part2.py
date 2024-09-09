import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	stringTotal = sum([len(line) for line in lines])
	memoryTotal = 0

	for line in lines:
		memoryTotal += sum([len(line), line.count('"'), line.count("\\")], 2)

	return memoryTotal - stringTotal
