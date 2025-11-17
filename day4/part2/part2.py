file = open("../data.txt", "r")
content = file.readlines()
file.close()

total = 0
grid = []
directions = [
    ( 1,  1),
    ( 1,  -1),
]
word = 'XMAS'

for line in content:
    grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'A':
            diagonal1 = False
            for x,y in directions:
                newX = i + x
                newY = j + y
                prevLetter = ''
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                    if grid[newX][newY] == 'M' or grid[newX][newY] == 'S':
                        prevLetter = grid[newX][newY]
                        newX = i - x
                        newY = j - y
                        if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                            if grid[newX][newY] == 'M' or grid[newX][newY] == 'S':
                                if prevLetter != grid[newX][newY]:
                                    if not diagonal1: diagonal1 = True
                                    else: total+=1

                                    


print(total)