f = open("2022\day2\input.txt", "r")
score = 0
n = 0

# ROCK: A/X. PAPER: B/Y. SCISSORS: C/Z
# WIN: 6. DRAW: 3 LOST. 

def convertToNumbers(opponent, player):
    op = opponent - 64
    ply = player - 87
    
    return (op, ply)

def determineWin(opponent, player):
    difference = player - opponent

    if difference == 0:
        return 3 + player
    elif difference == 1 or difference == -2:
        return 6 + player
    else:
        return 0 + player


for lines in f:
    numbers = convertToNumbers(ord(lines[0]), ord(lines[2]))
    points = determineWin(numbers[0], numbers[1])
    n += points
    
print(n)
f.close()