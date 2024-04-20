import os
from hashlib import md5

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	line = inputFile.readline()

answer = 0
while(md5((line + str(answer)).encode("utf-8")).hexdigest()[:5] != "00000"):
	answer += 1

print(answer)
