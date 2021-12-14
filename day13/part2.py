filepath = 'day13/input.txt'
with open(filepath, 'r') as f:
    coordinates, fold_instructions = f.read().split('\n\n')

# coordinates, fold_instructions = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5""".split('\n\n')

def fold(coordinates, fold_instruction, max_x, max_y):
    axis = fold_instruction['axis']
    value = fold_instruction['value']
    if axis == 'x':
        new_coordinates = list(filter(lambda dot: dot[0] < value, coordinates))
        fold_coordinates = list(filter(lambda dot: dot[0] > value, coordinates))
        for dot in fold_coordinates:
            new_coordinates.append((max_x - dot[0], dot[1]))
        max_x = value - 1
    elif axis == 'y':
        new_coordinates = list(filter(lambda dot: dot[1] < value, coordinates))
        fold_coordinates = list(filter(lambda dot: dot[1] > value, coordinates))
        for dot in fold_coordinates:
            new_coordinates.append((dot[0], max_y - dot[1]))
        max_y = value - 1
    return list(set(new_coordinates)), max_x, max_y

coordinates = list(map(lambda dot: (int(dot.split(',')[0]), int(dot.split(',')[1])), coordinates.split('\n')))

# print(coordinates)
fold_instructions = fold_instructions.split('\n')
fold_instructions = list(map(lambda instruction: instruction.strip('fold along '), fold_instructions))

fold_instructions = list(map(lambda instruction: {'axis': instruction.split('=')[0], 'value': int(instruction.split('=')[1])}, fold_instructions))
# for instruction in fold_instructions:
#     print(instruction)
# exit()
# print(len(coordinates), len(set(coordinates)))
# max_x = max(map(lambda dot: dot[0], coordinates))
# max_y = max(map(lambda dot: dot[1], coordinates))
# output_str = ''
# for y in range(0, max_y + 1):
#     for x in range(0, max_x +1):
#         if (x, y) in coordinates:
#             output_str += '##'
#         else:
#             output_str += '  '
#     output_str += '\n'
# print(output_str)
print(len(coordinates))
max_x = max(map(lambda dot: dot[0], coordinates))
max_y = max(map(lambda dot: dot[1], coordinates))
for instruction in fold_instructions:
    coordinates, max_x, max_y = fold(coordinates, instruction, max_x, max_y)
max_x = max(map(lambda dot: dot[0], coordinates))
max_y = max(map(lambda dot: dot[1], coordinates))
output_str = ''
for y in range(0, max_y + 1):
    for x in range(0, max_x +1):
        if (x, y) in coordinates:
            output_str += '#'
        else:
            output_str += '.'
    output_str += '\n'
print(output_str)
print(len(coordinates))


print(max_x, max_y)

print(len(coordinates))
