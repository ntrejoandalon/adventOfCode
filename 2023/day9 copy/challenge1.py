import re

x = "You have exceeded your available amount of [dollars & cents]"

k = re.sub("\(.*?\)|\[.*?\]","",x)
m = (re.sub(r'[^\w\s]','', k))
l = re.sub(' +', ' ', m)


print(l)