filepath = 'day02/input.txt'
with open(filepath, 'r') as f:
    course = f.read().split('\n')

horizontal = 0
depth = 0

for command in course:
    direction, value = command.split()
    if direction == 'forward':
        horizontal += int(value)
    elif direction == 'down':
        depth += int(value)
    elif direction == 'up':
        depth -= int(value)

print(horizontal * depth)
