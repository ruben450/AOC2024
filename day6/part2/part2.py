file = open("../data.txt", "r")
content = file.readlines()
file.close()

map = []

for line in content:
    map.append(list(line.strip()))

global guard
def find_guard(grid):
    global guard
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in ['^', '>', 'v', '<']:
                return x, y, cell
    raise ValueError("Geen guard gevonden in de map")




total = 0

rotations = ['^','>','v','<']
startX, startY, startArrow = find_guard(map)
originalMap = [row.copy() for row in map]
for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if map[i][j] in rotations or map[i][j] == '#':
                continue
            map[i][j] = '#'
            visited = set()
            x = startX
            y = startY
            arrow = startArrow
            rotation = rotations.index(arrow)
            guard = True
            while guard:
                status = (x,y, arrow)
                if status in visited:
                    total+=1
                    break
                visited.add(status)
                dx, dy = {
                    '^': (0, -1),
                    '>': (1, 0),
                    'v': (0, 1),
                    '<': (-1, 0)
                }[arrow]

                nx = x + dx
                ny = y + dy

                if not (0 <= nx < len(map[0]) and 0 <= ny < len(map)):
                    guard = False
                    break
                if map[ny][nx] in ['.','X']:
                    map[y][x] = 'X'
                    map[ny][nx] = arrow
                    x, y = nx, ny
                elif map[ny][nx] == '#':
                    if rotation < 3:
                        rotation += 1
                    else:
                        rotation = 0
                    map[y][x] = arrow = rotations[rotation]
            map = [row.copy() for row in originalMap]

print(total)
