import re
import math

time = []
distance = []

def calculateNumberOptions(t, d : int):
    minDistance = d + 1
    minStart = int(math.sqrt(minDistance))
    passesValue = (minStart * (t - minStart)) > minDistance

    while passesValue:
        minStart -= 1
        distanceTravelled = minStart * (t - minStart)
        if distanceTravelled < minDistance:
            passesValue = False
            minStart += 1
        elif distanceTravelled == minDistance:
            passesValue = False
       
        # time held down * (time - time_held down) time travelled = time, start at square root of time then move down
        
    #maxStartTime = time - minStart
    #difference: time - minStart - minStart
    return (t - 2 * minStart + 1)
        
    
f = open("2023\day6\input.txt", "r")
n = 0
for lines in f:
    currLine = lines.strip("\n")
    m = int("".join([c for c in currLine if c.isnumeric()]))
    
    revisedValues = m
    
    if n == 0:
        time = revisedValues
    else:
        distance = revisedValues
        
    n += 1  
     
f.close()



numWays = calculateNumberOptions(int(time), int(distance))
    
print(numWays)