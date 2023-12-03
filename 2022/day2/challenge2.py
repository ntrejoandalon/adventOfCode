f = open("2022\day2\example.txt", "r")
score = 0
n = 0

playRange = [1, 2, 3, 1, 2, 3] #rock, paper, scissors values
# ROCK: A. PAPER: B. SCISSORS: C
# WIN: 6/z. DRAW: 3/y LOST 0/x. 

def determineWin(opponent, result):
    op = opponent - 65

    if result == "X":
        return 0 + playRange[op-1]
    
    elif result == "Y":
        return 3 + playRange[op]
    else: 
        return 6 + playRange[op - 2]

for lines in f:
    points = determineWin(ord(lines[0]), lines[2])
    n += points
    
print(n)
f.close()