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
    if badUpdate:
        correctUpdates.append(update)

orderedCorrectUpdates = []
for update in correctUpdates:
    correctOrder = update.split(',').copy()
    swapped = True
    while swapped:
        swapped = False
        for x in correctOrder:
            for rule in rules:
                if x == rule[0] and rule[1] in correctOrder:
                    a = correctOrder.index(rule[0])
                    b = correctOrder.index(rule[1])
                    if a > b:
                        correctOrder[a], correctOrder[b] = correctOrder[b], correctOrder[a]
                        swapped = True
    orderedCorrectUpdates.append(correctOrder)

total = 0
for update in orderedCorrectUpdates:
    total += int(update[len(update)//2])
print(total)
