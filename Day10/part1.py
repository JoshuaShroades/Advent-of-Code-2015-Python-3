import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	line = lines[0]
	for _ in range(40):
		line = lookAndSay(line)
	return len(line)

def lookAndSay(look:str) -> str:
	value = look[0]
	count = 0
	say = ""
	for char in look:
		if(char == value):
			count += 1
		else:
			say += str(count) + value
			value = char
			count = 1
	say += str(count) + value
	return say
