filepath = 'day12/input.txt'
with open(filepath, 'r') as f:
    connections = f.read().split('\n')

connections = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split('\n')

caves_set = set()
for connection in connections:
    for cave in connection.split('-'):
        caves_set.add(cave)

caves = {}

for cave in caves_set:
    caves[cave] = []
    for connection in connections:
        connection = connection.split('-')
        if cave in connection:
            caves[cave].append(connection[0] if cave == connection[1] else connection[1])

paths = []

print(caves)

def make_paths(path=['start'], i=0):
    global caves
    global paths
    cave = path[-1]
    if cave == 'end':
        paths.append(path.copy())
        make_paths()
    connections = caves[cave]
    if i < len(connections):
        connection = connections[i]
        if not (connection in path and connection.islower()):
            path.append(connection)
            make_paths(path, i)
    i += 1
    # for connection in connections:
    #     if not (connection in path and connection.islower()):
    #         path.append(connection)
    #         make_paths(path)

make_paths()
print(paths)