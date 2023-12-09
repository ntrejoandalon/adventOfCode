#Another version of part 2. Removers reversing.
lines = []
f = open("2023\day9\input.txt", "r")
for line in f:
    currLine = line.strip("\n")
    l = [int(v) for v in currLine.split(" ")]
    lines.append(l)    
f.close()

n = 0
for i, line in enumerate(lines):
    diff = []
    diff.append(line)

    num0InLast = -1
    
    while num0InLast != len(diff[-1]):
        lineRange = []

        for j in range(len(diff[-1]) - 1):
            firstVal = diff[-1][j]
            secondVal = diff[-1][j+1]
            
            lineRange.append(firstVal - secondVal)
        
        diff.append(lineRange)
        num0InLast = len([x for x in diff[-1] if x == 0])

    n += sum([x[0] for x in diff])     
print(n)   
        