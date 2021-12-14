filepath = 'day13/input.txt'
with open(filepath, 'r') as f:
    coordinates, fold_instructions = f.read().split('\n\n')

def fold(coordinates, fold_instruction):
    axis = fold_instruction['axis']
    value = fold_instruction['value']
    if axis == 'x':
        new_coordinates = list(filter(lambda dot: dot[0] < value, coordinates))
        fold_coordinates = list(filter(lambda dot: dot[0] > value, coordinates))
        max_x = max(map(lambda dot: dot[0], fold_coordinates))
        for dot in fold_coordinates:
            new_coordinates.append((max_x - dot[0], dot[1]))
    return new_coordinates

coordinates = list(map(lambda dot: (int(dot.split(',')[0]), int(dot.split(',')[1])), coordinates.split('\n')))

# print(coordinates)
fold_instruction = fold_instructions.split('\n')[0].strip('fold along ')
# print(fold_instruction)
fold_instruction = {'axis': fold_instruction.split('=')[0], 'value': int(fold_instruction.split('=')[1])}
# print(fold_instruction)

# print(len(coordinates), len(set(coordinates)))

new_coordinates = fold(coordinates, fold_instruction)

print(new_coordinates, len(new_coordinates), len(set(new_coordinates)))