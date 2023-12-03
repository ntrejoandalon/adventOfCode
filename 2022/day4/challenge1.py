import re

f = open("2022\day4\input.txt", "r")
overlapping = 0
    
    
def determineIfEngulfing(range1, range2):
    pass

for lines in f:
    currLine = lines.replace("\n", "")
    val = [int(val) for val in re.split(r',|-', currLine)]
    range1 = range(val[0], val[1]+1)
    range2 = range(val[2], val[3]+1)
        
    if all(e in range2 for e in range1) or all(e in range1 for e in range2):
        overlapping += 1

    
print(overlapping)
f.close()