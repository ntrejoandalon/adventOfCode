f = open("2022\day7\example.txt", "r")
string = ""

for line in f:
    string = string + line

f.close()

charList = list(string)
notFound = True
n = 0
foundIndex = -1

while notFound:
   value = len(set(charList[n: n+4]))
   if value == 4:
       notFound = False
       foundIndex = n
   n += 1 

print(foundIndex + 4)
