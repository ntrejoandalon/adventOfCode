digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def convertToNum(line):
    newLine = line
    for i in range(0, len(digits)):
        newLine = newLine.replace(digits[i], digits[i][0] + str(i+1) + digits[i][-1])
    return newLine    

f = open("day1\day1input.txt", "r")
calibrationValues = []

#clean up lines
for line in f:
    currLine = [*convertToNum(line)]
    print(currLine)
    numbers = [num for num in currLine if num.isnumeric()]
    value = 0
    if len(numbers) >= 2:
        value = (int(numbers[0] + numbers[-1]))
    else: 
        value = (int(numbers[0]) * 11)

    calibrationValues.append(value)
  
print(sum(calibrationValues))  
f.close()

