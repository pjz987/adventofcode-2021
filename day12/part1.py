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

class Cave:
    def __init__(self, name):
        self.blocked = False
        self.name = name
        if name in ['start', 'end']:
            self.type = name
        if name.isupper(): self.type = 'big'
        if name.islower():
            self.type = 'small'
        
        self.connections = []
    
    def set_connections(self, connections):
        for connection in connections:
            if connection.cave1 is self or connection.cave2 is self:
                cave = connection.cave1 if connection.cave2 is self else connection.cave2
                self.connections.append(cave)
    
    def block_check(self):
        if self.type == 'small':
            self.blocked = True

    def reset(self):
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

# for cave in caves:
#     print()
#     print(cave)
#     for connection in cave.connections:
#         print(connection)

start = None
# end = None
for cave in caves:
    if cave.name == 'start': start = cave
    # if cave.name == 'end': end = cave

path = Path(start)
while True:
    print(path)
    path.move()
    if path.check_end():
        break

print(path)

