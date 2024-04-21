import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

lightGrid = [[0]*1000 for _ in range(1000)]

for line in lines:
	lineInstructions = line.split(" ")

	if(lineInstructions[0] == "toggle"):
		instruction = lineInstructions[0]
		areaStart = tuple(int(x) for x in lineInstructions[1].split(","))
		areaEnd = tuple(int(x) for x in lineInstructions[3].split(","))
	else:
		instruction = lineInstructions[1]
		areaStart = tuple(int(x) for x in lineInstructions[2].split(","))
		areaEnd = tuple(int(x) for x in lineInstructions[4].split(","))

	match instruction:
		case "toggle":
			for y in range(areaStart[1], areaEnd[1]+1):
				for x in range(areaStart[0], areaEnd[0]+1):
					lightGrid[y][x] = (lightGrid[y][x] + 1) % 2

		case "on":
			for y in range(areaStart[1], areaEnd[1]+1):
				for x in range(areaStart[0], areaEnd[0]+1):
					lightGrid[y][x] = 1

		case "off":
			for y in range(areaStart[1], areaEnd[1]+1):
				for x in range(areaStart[0], areaEnd[0]+1):
					lightGrid[y][x] = 0

lightSum = 0

for lightRow in lightGrid:
	lightSum += sum(lightRow)

print(lightSum)
