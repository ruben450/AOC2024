file = open("../data.txt", "r")
content = file.readlines()
file.close()

from itertools import product

total = 0
for line in content:
    answer = int(line.strip().split(':')[0])
    numbers = line.strip().split(':')[1].strip().split(' ')
    numbers = [int(number) for number in numbers]
    for operators in product(['+', '*'], repeat = len(numbers) -1):
        sum = numbers[0]
        print (operators)
        for i, op in enumerate(operators):
            if op == '+':
                sum += numbers[i+1]
            if op == '*':
                sum *= numbers[i+1]
            print(f"index: {i} sum = {sum} ans = {answer}")
        if answer == sum:
            total+=sum
            break
print(total)