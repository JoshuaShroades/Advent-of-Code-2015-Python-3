import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

locations = set()
distances = {}
trips = []

def main():
	for line in lines:
		locationAB, distance = line.split(" = ")
		locationA, locationB = locationAB.split(" to ")
		locations.add(locationA)
		locations.add(locationB)
		distance = int(distance)
		distances[(locationA, locationB)] = distance
	
	global shortestLength
	shortestLength = sum(distances.values())
	
	for startingLocation in locations:
		for distance in distances:
			if(startingLocation == distance[0]):
				step([], distance[0])
			if(startingLocation == distance[1]):
				step([], distance[1])

	for trip in trips:
		length = tripLength(trip)
		if(length < shortestLength):
			shortestLength = length
	
	return shortestLength
	

def step(history:list, destination):
	global shortestLength
	history.append(destination)
	if(tripLength(history.copy()) <= shortestLength):
		if(len(history) == len(locations) and history not in trips):
			trips.append(history)
			if(tripLength(history.copy()) < shortestLength):
				shortestLength = tripLength(history.copy())
		else:
			validTrips = [distance for distance in distances if destination in distance]
			validDestinations = set()
			for trip in validTrips:
				if(trip[0] not in history):
					validDestinations.add(trip[0])
				if(trip[1] not in history):
					validDestinations.add(trip[1])
			for validDestination in validDestinations:
				step(history.copy(), validDestination)

def tripLength(trip:list) -> int:
	totalLength = 0
	for locationIndex in range(len(trip)-1):
		if((trip[locationIndex], trip[locationIndex+1]) in distances):
			totalLength += distances[(trip[locationIndex], trip[locationIndex+1])]
		elif((trip[locationIndex+1], trip[locationIndex]) in distances):
			totalLength += distances[(trip[locationIndex+1], trip[locationIndex])]
	return totalLength
