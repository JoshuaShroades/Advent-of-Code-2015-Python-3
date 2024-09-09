import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	strings = [line[:-1] for line in inputFile]

def main():
	niceStringCount = 0

	for string in strings:
		stringPair = False
		doubleChar = False

		for i in range(len(string)-2):
			pair = string[i:i+2]

			if(string.count(pair) > 1):
				stringPair = True

			char = string[i]

			if(char == string[i+2]):
				doubleChar = True
				continue

		if(stringPair and doubleChar):
			niceStringCount += 1

	return niceStringCount
