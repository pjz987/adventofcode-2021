from math import prod


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

def get_basin(y, x, basin=[]):
    global heightmap
    # up
    if y > 0:
        if heightmap[y][x] < heightmap[y - 1][x]:
            if (y - 1, x) not in basin and heightmap[y - 1][x] != 9:
                basin.append((y - 1, x))
                basin = get_basin(y - 1, x, basin)
    # right
    if x < len(heightmap[y]) - 1:
        if heightmap[y][x] < heightmap[y][x + 1]:
            if (y, x + 1) not in basin and heightmap[y][x + 1] != 9:
                basin.append((y, x + 1))
                basin = get_basin(y, x + 1, basin)
    # down
    if y < len(heightmap) - 1:
        if heightmap[y][x] < heightmap[y + 1][x]:
            if (y + 1, x) not in basin and heightmap[y + 1][x] != 9:
                basin.append((y + 1, x))
                basin = get_basin(y + 1, x, basin)
    # left
    if x > 0:
        if heightmap[y][x] < heightmap[y][x - 1]:
            if (y, x - 1) not in basin and heightmap[y][x - 1] != 9:
                basin.append((y, x - 1))
                basin = get_basin(y, x - 1, basin)
    return basin

basin_sizes = []

for y, row in enumerate(heightmap):
    for x, height in enumerate(row):
        if is_low_point(y, x):
            basin = get_basin(y, x, [(y, x)])
            basin_sizes.append(len(basin))

basin_sizes.sort()
print(prod(basin_sizes[-3:]))

