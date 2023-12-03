import re

f = open("2022\day4\input.txt", "r")
overlapping = 0
    
    
def determineIfEngulfing(range1, range2):
    pass

for lines in f:
    currLine = lines.replace("\n", "")
    a1, a2, b1, b2 = [int(val) for val in re.split(r',|-', currLine)]
        
    if max(a1,b1) <= min(a2,b2):
        print(currLine)
        overlapping += 1

    
print(overlapping)
f.close()