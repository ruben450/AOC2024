file = open("../data.txt", "r")
content = file.readlines()
file.close()

total = 0
grid = []
directions = [
    (0,  1),
    ( 1,  1),
    ( 1, 0),
    ( 1,  -1),
    (0, -1),
    (-1,  -1),
    ( -1, 0),
    ( -1,  1)
]
word = 'XMAS'

for line in content:
    grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            for x,y in directions:
                newX = i + x
                newY = j + y
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                    if grid[newX][newY] == 'M':
                        newX = newX + x
                        newY = newY + y
                        if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                            if grid[newX][newY] == 'A':
                                newX = newX + x
                                newY = newY + y
                                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                                    if grid[newX][newY] == 'S':
                                        total += 1


print(total)