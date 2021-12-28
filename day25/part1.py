filepath = 'day25/input.txt'
with open(filepath, 'r') as f:
    rows = f.read().split('\n')

# rows = """v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>""".split('\n')

# rows = """...>...
# .......
# ......>
# v.....>
# ......>
# .......
# ..vvv..""".split('\n')

ROWS = len(rows)
COLUMNS = len(rows[0])
print(ROWS, COLUMNS)

def visualize(grid):
    y = 0
    output = ''
    for coordinates in grid:
        if coordinates[1] > y:
            output += '\n'
            y += 1
        cell = grid[coordinates]
        if cell is None:
            output += '.'
        elif cell.type == 'east':
            output += '>'
        elif cell.type == 'south':
            output += 'v'
    return output

class SeaCucumber:
    global grid
    global ROWS
    global COLUMNS
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.will_move = False
    
    def move(self):
        grid[(self.x, self.y)] = None
        if self.type == 'east':
            self.x += 1
            self.x %= COLUMNS
        elif self.type == 'south':
            self.y += 1
            self.y %= ROWS
        grid[(self.x, self.y)] = self
        
    def check(self):
        if self.type == 'east':
            x = (self.x + 1) % COLUMNS
            if grid[(x, self.y)] is None:
                return True
            return False
        if self.type == 'south':
            y = (self.y + 1) % ROWS
            if grid[(self.x, y)] is None:
                return True
            return False


    def __str__(self) -> str:
        return self.type

    def __repr__(self) -> str:
        return self.type

grid = {}
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == '>':
            grid[(x, y)] = SeaCucumber(x, y, 'east')
        elif cell == 'v':
            grid[(x, y)] = SeaCucumber(x, y, 'south')
        else:
            grid[(x, y)] = None

sea_cucumbers = list(filter(lambda sc: sc is not None, grid.values()))
east_sea_cucumbers = list(filter(lambda sc: sc.type == 'east', sea_cucumbers))
south_sea_cucumbers = list(filter(lambda sc: sc.type == 'south', sea_cucumbers))
step = 0
# print(visualize(grid))
while True:
    step += 1
    movement = False
    for sea_cucumber in east_sea_cucumbers:
        sea_cucumber.will_move = sea_cucumber.check()
    for sea_cucumber in east_sea_cucumbers:
        if sea_cucumber.will_move:
            movement = True
            sea_cucumber.move()
    for sea_cucumber in south_sea_cucumbers:
        sea_cucumber.will_move = sea_cucumber.check()
    for sea_cucumber in south_sea_cucumbers:
        if sea_cucumber.will_move:
            movement = True
            sea_cucumber.move()
    if movement == False:
        break
    for sea_cucumber in sea_cucumbers:
        sea_cucumber.will_move = False
    # print()
    # print(f'step {step}')
    # print(visualize(grid))

print(step)