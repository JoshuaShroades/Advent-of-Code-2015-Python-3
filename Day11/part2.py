import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

INVALID = "iol"

def main():
	password = lines[0]
	values = []
	for char in password:
		values.append(ord(char) % 97 + 1)
	increment(values)
	while(not validate(values)):
		increment(values)
	increment(values)
	while(not validate(values)):
		increment(values)
	return "".join([chr(val+96) for val in values])

def increment(values:list):
	values[-1] += 1
	while(any(val == 27 for val in values)):
		pos = values.index(27)
		values[pos] = 1
		if(pos):
			values[pos-1] += 1

def validate(password:list) -> bool:
	if(any(chr(char) in INVALID for char in password)):
		return False
	increasing = False
	for i in range(len(password)-2):
		if(password[i]+1 == password[i+1] and password[i]+2 == password[i+2]):
			increasing = True
	repeating = []
	for i in range(len(password)-1):
		if(password[i] == password[i+1]):
			if(repeating):
				if(repeating[-1]+1 < i and password[repeating[-1]] != password[i]):
					repeating.append(i)
			else:
				repeating.append(i)
		
	return increasing and len(repeating) > 1
