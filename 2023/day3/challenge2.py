linesSearched = []
numberLocations = {}
gearLocations = {}
answer = 0
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

def addGearLocationIfNearby(numRow, numberLocation):
    value, numStart, numEnd = numberLocation
    startRow = numRow - 1 if numRow != 0 else 0
    endRow = numRow + 1 if numRow < len(linesSearched)-1 else len(linesSearched) -1
    startIndex = numStart - 1 if numStart != 0 else 0
    endIndex = numEnd + 2 if numEnd+2 < len(linesSearched[numRow]) else len(linesSearched[numRow])    
    
    for i in range(startRow, endRow+1):
        area = "".join(linesSearched[i][startIndex:endIndex])
        gears = [int(i)+startIndex for i, ltr in enumerate(area) if ltr == "*"]
        
        for g in gears: 
            if (i, g) in gearLocations:
                gearLocations[(i, g)].append(value)
            else: 
                gearLocations[(i, g)] = [value]
                
    pass

n = 0
for line in f:
    currLine = line.replace("\n", "")
    linesSearched.append(list(currLine))
    numberLocations[n]=numLineRanges(currLine)
    n += 1

f.close()    

for k in numberLocations:
    for v in numberLocations[k]:
        addGearLocationIfNearby(k, v)

for k in gearLocations:
    if len(gearLocations[k]) == 2:
        val1, val2 = gearLocations[k]
        answer += (int(val1) * int(val2))
        
print(answer)

