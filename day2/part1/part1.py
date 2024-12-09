file = open("../data.txt", "r")
content = file.readlines()
file.close()

safeReports = 0
for line in content:
    levels = line.split()
    i = 1
    increasing = 2
    safe = 0
    while i < len(levels):
        a = int(levels[i - 1])
        b = int(levels[i])
        if a > b:
            if increasing != 0:
                increasing = 1
            else:
                safe = 0
                break
        else:
            if increasing != 1:
                increasing = 0
            else:
                safe = 0
                break
        
        diff = abs(a - b)
        if diff >= 1 and diff <= 3:
            safe = 1
        else:
            safe = 0
            break
        i+=1
    
    if safe == 1:
        safeReports+=1
print(safeReports)

    