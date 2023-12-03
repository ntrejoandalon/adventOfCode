#GOAL. GET THE NUMBERS ON EACH LINE AND ADD TOGETHER

f = open("day1\day1input copy.txt", "r")
calibrationValues = []

for line in f:
    listVersionOfLine = [*line]
    numbers = [num for num in line if num.isnumeric()]
    value = 0
    if len(numbers) >= 2:
        value = (int(numbers[0] + numbers[-1]))
    else: 
        value = (int(numbers[0]) * 11)

    calibrationValues.append(value)
  
print(sum(calibrationValues))  
f.close()
