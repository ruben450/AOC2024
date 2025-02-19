file = open("../data.txt", "r")
content = file.readlines()
file.close()

totalSafe = 0

def IsSafe(numbers):
    i = 1
    inc = 2
    safe = 0
    while i < len(numbers):
        a = int(numbers[i - 1])
        b = int(numbers[i])
        if a > b:
            if inc != 0:
                inc = 1
                safe = 1
            else:
                safe = 0
        else:
            if inc != 1:
                inc = 0
                safe = 1
            else:
                safe = 0
        if safe == False:
            return False
        diff = abs(a - b)
        if diff >= 1 and diff <= 3:
            safe = 1
        else:
            safe = 0
        if safe == 0:
            return False
        i+=1
    return bool(safe)

for line in content:
    numbers = line.split()
    safe = 0
    if IsSafe(numbers):
        safe = 1
    else:
        for i in range(len(numbers)):
            temp = numbers.copy()
            del temp[i]
            if IsSafe(temp):
                safe = 1
    totalSafe += safe

print(totalSafe)
                
        
