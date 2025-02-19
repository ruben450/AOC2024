import re

file = open("../data.txt", "r")
content = file.readlines()
file.close()

total = 0
enabled = True
for line in content:
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))",line)
    for match in matches:
        if match[2] == "" and enabled:
            total += int(match[0]) * int(match[1])
        else:
            if match[2] == "do()":
                enabled = True
            else:
                enabled = False

print(total)