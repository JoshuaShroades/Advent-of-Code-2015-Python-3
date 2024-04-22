import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

instructions = []
wires = {}

for line in lines:
	instruction, wire = line.split(" -> ")
	if(instruction.isnumeric()):
		wires[wire] = int(instruction)
	else:
		splitInstruction = instruction.split(" ")
		instructions.append((splitInstruction, wire))
		wires[wire] = None

wires = dict(sorted(wires.items()))

def getValue(x:str) -> int:
	if(x.isnumeric()):
		return int(x)
	else:
		return wires[x]

while(wires["a"] == None):
	for instruction, destination in instructions:
		if(len(instruction) == 1 and getValue(instruction[0]) != None):
			wires[destination] = getValue(instruction[0])

		elif(len(instruction) == 2 and getValue(instruction[1]) != None):
			if(instruction[0] == "NOT"):
				wires[destination] = 65535 - getValue(instruction[1])

		elif(len(instruction) == 3 and getValue(instruction[0]) != None and getValue(instruction[2]) != None):
			if(instruction[1] == "AND"):
				wires[destination] = getValue(instruction[0]) & getValue(instruction[2])
			elif(instruction[1] == "OR"):
				wires[destination] = getValue(instruction[0]) | getValue(instruction[2])
			elif(instruction[1] == "LSHIFT"):
				wires[destination] = (getValue(instruction[0]) * 2 ** getValue(instruction[2])) % 65536
			elif(instruction[1] == "RSHIFT"):
				wires[destination] = getValue(instruction[0]) // 2 ** getValue(instruction[2])

print(wires["a"])
