filepath = 'day02/input.txt'
with open(filepath, 'r') as f:
    course = f.read().split('\n')

aim = 0
horizontal = 0
depth = 0

for command in course:
    direction, value = command.split()
    if direction == 'forward':
        horizontal += int(value)
        depth += aim * int(value)
    elif direction == 'down':
        aim += int(value)
    elif direction == 'up':
        aim -= int(value)

print(horizontal * depth)
