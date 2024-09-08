import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

stringTotal = sum([len(line) for line in lines])
memoryTotal = 0

for line in lines:
	string = False
	escape = False
	hexcode = 0
	lineTotal = 0
	for char in line:
		if(char == '"'):
			if(escape):
				lineTotal += 1
				escape = False
			else:
				string = not string
		elif(char == "\\"):
			if(escape):
				lineTotal += 1
			escape = not escape
		elif(char == "x" and escape and not hexcode):
			hexcode += 1
		elif(hexcode):
			if(hexcode < 2):
				hexcode += 1
			else:
				hexcode = 0
				escape = False
				lineTotal += 1
		else:
			lineTotal += 1
	memoryTotal += lineTotal

print(stringTotal - memoryTotal)
