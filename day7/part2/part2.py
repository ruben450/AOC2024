file = open("../data.txt", "r")
content = file.readlines()
file.close()

map = []

for line in content:
    map.append(list(line.strip()))