linesSearched = []
numberLocations = {}

f = open("2023\day3\input.txt", "r")
numbers = []
def numLineRanges(line):
    numbers = []
    inNumber = False
    start = 0
    
    for i in range(len(line)):
        c = line[i]
        if not inNumber and c.isnumeric():
            inNumber=True
            start = i
        elif inNumber and not c.isnumeric():
            inNumber = False
            numbers.append((line[start:i], start, i-1))
            
    if inNumber:
        numbers.append((line[start:], start, len(line) -1))
    
    return numbers

def checkIfPart(numRow, numStart, numEnd):
    startRow = numRow - 1 if numRow != 0 else 0
    endRow = numRow + 1 if numRow < len(linesSearched)-1 else len(linesSearched) -1
    startIndex = numStart - 1 if numStart != 0 else 0
    endIndex = numEnd + 2 if numEnd+2 < len(linesSearched[numRow]) else len(linesSearched[numRow])    
    
    area = linesSearched[startRow][startIndex:endIndex] + linesSearched[numRow][startIndex:endIndex] + linesSearched[endRow][startIndex:endIndex]
    
    specialChars = [c for c in area if not c.isnumeric() and c != "."]
    return len(specialChars) > 0

n = 0
for line in f:
    currLine = line.replace("\n", "")
    linesSearched.append(list(currLine))
    numberLocations[n]=numLineRanges(currLine)
    n += 1

f.close()    

for k in numberLocations:
    for v in numberLocations[k]:
        value, start, end = v
        if checkIfPart(k, start, end):
            numbers.append(int(value))

print(sum(numbers))

