file = open("data.txt", "r")
content = file.readlines()
file.close()

totalDistance = 0

leftNumbers = []
rightNumbers = []

for line in content:
    numbers = line.split()
    a = int(numbers[0])
    b = int(numbers[1])
    leftNumbers.append(a)
    rightNumbers.append(b)

while len(leftNumbers) > 0:
    a = min(leftNumbers)
    b = min(rightNumbers)
    totalDistance += abs(a-b)
    leftNumbers.remove(a)
    rightNumbers.remove(b)

print(totalDistance)


    