file = open("../data.txt", "r")
content = file.readlines()
file.close()

map = []

for line in content:
    map.append(list(line.strip()))

global guard
guard = True

def move(x:int,y:int, direction:tuple):
    global guard
    if not (0 <= x < len(map[0]) -1 and 0 <= y < len(map)-1):
        map[y][x] = 'X'
        guard = False
        return
    
    if direction == (0, 1):
        if map[y+1][x] in ['.', 'X']:
            map[y][x] = 'X'
            map[y+1][x] = 'v'
        elif map[y+1][x] == '#':
            map[y][x] = '<'
    elif direction == (1, 0):
        if map[y][x+1] in ['.', 'X']:
            map[y][x] = 'X'
            map[y][x+1] = '>'
        elif map[y][x+1] == '#':
            map[y][x] = 'v'
    elif direction == (0, -1):
        if map[y-1][x] in ['.', 'X']:
            map[y][x] = 'X'
            map[y-1][x] = '^'
        elif map[y-1][x] == '#':
            map[y][x] = '>'
    elif direction == (-1, 0):
        if map[y][x-1] in ['.', 'X']:
            map[y][x] = 'X'
            map[y][x-1] = '<'
        elif map[y][x-1] == '#':
            map[y][x] = '^'

gridCopy = map.copy()
while guard:
    for y, a in enumerate(gridCopy):
        for x, b in enumerate(gridCopy):
            if map[y][x] == '^':
                move(x,y,(0,-1))
            if map[y][x] == '>':
                move(x,y,(1,0))
            if map[y][x] == 'v':
                move(x,y,(0,1))
            if map[y][x] == '<':
                move(x,y,(-1,0))

total = 0
for row in map:
    for cell in row:
        if cell == 'X':
            total +=1
    print(row)

print(total)


