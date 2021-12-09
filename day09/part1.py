filepath = 'day09/input.txt'
with open(filepath, 'r') as f:
    heightmap = [[int(num) for num in row] for row in f.read().split('\n')]
print(heightmap)

def is_low_point(y, x):
    global heightmap
    # up
    if y > 0:
        if heightmap[y][x] >= heightmap[y - 1][x]:
            return False
    # right
    if x < len(heightmap[y]) - 1:
        if heightmap[y][x] >= heightmap[y][x + 1]:
            return False
    # down
    if y < len(heightmap) - 1:
        if heightmap[y][x] >= heightmap[y + 1][x]:
            return False
    # left
    if x > 0:
        if heightmap[y][x] >= heightmap[y][x - 1]:
            return False
    return True

risk_levels = 0

for y, row in enumerate(heightmap):
    for x, height in enumerate(row):
        if is_low_point(y, x):
            risk_levels += height + 1

print(risk_levels)
