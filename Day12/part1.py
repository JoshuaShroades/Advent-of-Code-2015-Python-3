import os
import json

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.json")

with open(inputFilePath) as inputFile:
	jsonData = json.load(inputFile)

total = 0

def main():
	global total
	total = 0
	dictSum(jsonData.values())
	return total

def dictSum(values):
	for value in values:
		if(type(value) is dict):
			dictSum(value.values())
		elif(type(value) is list):
			dictSum(value)
		elif(type(value) is int):
			global total
			total += value
