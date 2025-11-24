file = open("../data.txt", "r")
content = file.readlines()
file.close()

rules = []
updates = []
locUpdate = 0
for index, line in enumerate(content):
    if line.strip() == "":
        locUpdate = index + 1
        break
    rules.append(line.strip().split('|'))

for line in content[locUpdate:]:
    updates.append(line.strip())

correctUpdates = []
for update in updates:
    updateBlocks = update.split(',')
    badUpdate = False
    for index, x in enumerate(updateBlocks):
        for rule in rules:
            if x == rule[0]:
                if rule[1] in updateBlocks:
                    if rule[1] not in updateBlocks[index+1:]:
                        badUpdate = True
                        break
            if index > 0:
                if x == rule[1]:
                    if rule[0] in updateBlocks:
                        if rule[0] not in updateBlocks[:index+1]:
                            badUpdate = True
                            break
    if not badUpdate:
            correctUpdates.append(update)

total = 0
for update in correctUpdates:
    update = update.split(',')
    total += int(update[len(update)//2])
print(total)