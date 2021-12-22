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

class BlockedError(Exception):
    ...
class Cave:
    def __init__(self, name):
        self.blocked = False
        self.name = name

        if name in ['start', 'end']:
            self.type = name
        elif name.isupper():
            self.type = 'big'
        elif name.islower():
            self.type = 'small'

        self.connection_index = 0
        
        self.connections = []
    
    def set_connections(self, connections):
        for connection in connections:
            if connection.cave1 is self or connection.cave2 is self:
                cave = connection.cave1 if connection.cave2 is self else connection.cave2
                self.connections.append(cave)
    
    def make_path(self, path):
        if self.blocked:
            raise BlockedError
        self.block_check()

        if self.type == 'end':
            return path
        try:
            path.append(self.connections[self.connection_index])
        except IndexError:
            return path
        try:
            return self.connections[self.connection_index].make_path(path)
        except BlockedError:
            path.pop()
            self.connection_index += 1
            return path
    
    def block_check(self):
        if self.type in ('small', 'start'):
            self.blocked = True

    def reset(self):
        # self.connection_index = 0
        self.blocked = False
    
    def __str__(self):
        return self.name
    
class Connection:
    def __init__(self, cave1, cave2):
        self.cave1 = cave1
        self.cave2 = cave2
    
    def __str__(self):
        return f'{self.cave1}-{self.cave2}'

class Path:
    def __init__(self, start):
        self.path = [start]
    
    def move(self):
        current_cave = self.path[-1]
        for next_cave in current_cave.connections:
            if not next_cave.blocked:
                self.path.append(next_cave)
                next_cave.block_check()
            # if connection.cave1 is not cave and not connection.cave1.blocked:
            #     self.path.append(cave1)
            #     if cave1.type == 'small':
            #         cave1.blocked = True
            #     return
            # if connection.cave2 is not cave and not connection.cave2.blocked:
            #     self.path.append(cave2)
            #     if cave2.type == 'small':
            #         cave2.blocked = True
            #     return
    
    def check_end(self):
        return self.path[-1].name == 'end'

    
    def __str__(self):
        return ','.join(map(lambda cave: str(cave), self.path))

def unblock(caves):
    for cave in caves:
        cave.reset()

caves = set()
for connection in connections:
    [caves.add(cave) for cave in connection.split('-')]

string_connections = connections.copy()
connections = []

caves = [Cave(cave) for cave in caves]
for connection in string_connections:
    cave1_name, cave2_name = connection.split('-')
    cave1 = None
    cave2 = None
    for cave in caves:
        if cave.name == cave1_name:
            cave1 = cave
        if cave.name == cave2_name:
            cave2 = cave
    connections.append(Connection(cave1, cave2))

for cave in caves:
    cave.set_connections(connections)

for cave in caves:
    # print(cave.name)
    if cave.type == 'start':
        start = cave
paths = []
for _ in range(10):
    path = [start]
    paths.append(start.make_path(path))
    print(paths)
    print(len(path))
    unblock(caves)
print(len(paths))

for path in paths:
    print('*'*40)
    print(len(path))
    print(','.join([str(cave) for cave in path]))
