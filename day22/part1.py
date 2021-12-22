filepath = 'day22/input.txt'
with open(filepath, 'r') as f:
    reboot_steps = f.read().split('\n')

cubes = {}
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            cubes[(x, y, z)] = False

for i, step in enumerate(reboot_steps):
    if i == 20: break
    on_off = step.split(' ')[0]
    ranges = step.split(' ')[1].split(',')

    x_range = ranges[0].strip('x=').split('..')
    y_range = ranges[1].strip('y=').split('..')
    z_range = ranges[2].strip('z=').split('..')

    x_range = range(int(x_range[0]), int(x_range[1]) + 1)
    y_range = range(int(y_range[0]), int(y_range[1]) + 1)
    z_range = range(int(z_range[0]), int(z_range[1]) + 1)

    on_off = True if on_off == 'on' else False
    for x in x_range:
        for y in y_range:
            for z in z_range:
                cubes[(x, y, z)] = on_off


print(len(list(filter(lambda cube: cube == True, cubes.values()))))