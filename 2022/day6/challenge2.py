f = open("2022\day6\input.txt", "r")
string = ""

for line in f:
    string = string + line

f.close()

charList = list(string)
notFound = True
n = 0
foundIndex = -1
lengthNeeded = 14

while notFound:
   value = len(set(charList[n: n+lengthNeeded]))
   if value == lengthNeeded:
       notFound = False
       foundIndex = n
   n += 1 

print(foundIndex + lengthNeeded)
