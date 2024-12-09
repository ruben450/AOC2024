file = open("../data.txt", "r")
content = file.readlines()
file.close()

total = 0

leftNumbers = []
rightNumbers = []

for line in content:
    numbers = line.split()
    a = int(numbers[0])
    b = int(numbers[1])
    leftNumbers.append(a)
    rightNumbers.append(b)

for a in leftNumbers:
    appears = rightNumbers.count(a)
    total += a * appears 

print(total)
