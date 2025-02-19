import re

file = open("../data.txt", "r")
content = file.readlines()
file.close()

total = 0
for line in content:
    mem = re.findall("mul\(\d+,\d+\)",line)
    for mul in mem:
        digits = re.findall("\d+", mul)
        a = digits[0]
        b = digits[1]
        total += int(a) * int(b)

print(total)
        