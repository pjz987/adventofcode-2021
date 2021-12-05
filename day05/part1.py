filepath = 'day05/input.txt'
with open(filepath, 'r') as f:
    lines = f.read().split('\n')

# lines = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".split('\n')

lines = list(map(lambda line: ','.join(line.split(' -> ')).split(','), lines))
lines = list(map(lambda line: {
    'x1': int(line[0]),
    'y1': int(line[1]),
    'x2': int(line[2]),
    'y2': int(line[3]),
}, lines))

ocean_floor = [[0 for _ in range(1000)] for _ in range(1000)]
# ocean_floor = [[0 for _ in range(10)] for _ in range(10)]

for line in lines:
    x1, y1, x2, y2 = line['x1'], line['y1'], line['x2'], line['y2']
    if x1 == x2:
        x = x1
        start = min(y1, y2)
        end = max(y1, y2)
        for y in range(start, end + 1):
            ocean_floor[y][x] += 1

    elif y1 == y2:
        y = y1
        start = min(x1, x2)
        end = max(x1, x2)
        for x in range(start, end + 1):
            ocean_floor[y][x] += 1
    
    else:
        ...

hazards = 0

for row in ocean_floor:
    for coordinate in row:
        if coordinate > 1: hazards += 1

print(hazards)