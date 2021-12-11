filepath = 'day11/input.txt'
with open(filepath, 'r') as f:
    lines = f.read().split('\n')

# lines = """11111
# 19991
# 19191
# 19991
# 11111""".split('\n')

flash_counter = 0

class Octopus:
    def __init__(self, energy):
        self.flashed_this_step = False
        self.energy = energy
        self.neighbors = []

    def set_neighbors(self, grid, y, x):
        if y > 0:
            # north
            self.neighbors.append(grid[y - 1][x])
            if x < len(grid) - 1:
                # northeast
                self.neighbors.append(grid[y - 1][x + 1])
        if x < len(grid) - 1:
            # east
            self.neighbors.append(grid[y][x + 1])
            if y < len(grid) - 1:
                # southeast
                self.neighbors.append(grid[y + 1][x + 1])
        if y < len(grid) - 1:
            # south
            self.neighbors.append(grid[y + 1][x])
            if x > 0:
                # southwest
                self.neighbors.append(grid[y + 1][x - 1])
        if x > 0:
            # west
            self.neighbors.append(grid[y][x - 1])
            if y > 0:
                # northwest
                self.neighbors.append(grid[y - 1][x - 1])        
    
    def charge(self):
        self.energy += 1
    
    def flash_check(self):
        if self.flashed_this_step or self.energy < 10: return
        self.flash()

    def flash(self):
        global flash_counter
        global flashed_this_loop
        self.flashed_this_step = True
        flashed_this_loop = True
        flash_counter += 1
        [neighbor.charge() for neighbor in self.neighbors]
    
    def reset_check(self):
        if self.flashed_this_step: self.reset()
    
    def reset(self):
        self.energy = 0
        self.flashed_this_step = False
    
    def __str__(self):
        return str(self.energy)

grid = [[Octopus(int(energy)) for energy in row] for row in lines]

[[octopus.set_neighbors(grid, y, x) for x, octopus in enumerate(row)] for y, row in enumerate(grid)]

# I always need to look this up https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
# flat_list = [item for sublist in t for item in sublist]
octopuses = [octopus for row in grid for octopus in row]

def make_grid(octopuses):
    grid = ''
    for i, octopus in enumerate(octopuses):
        grid += str(octopus)
        # if i % 5 == 4:
        if i % 10 == 9:
            grid += '\n'
    return grid


for _ in range(100):
    print(make_grid(octopuses))
    [octopus.charge() for octopus in octopuses]
    while True:
        flashed_this_loop = False
        [octopus.flash_check() for octopus in octopuses]
        if flashed_this_loop == False: break
    [octopus.reset_check() for octopus in octopuses]

print(make_grid(octopuses))
    
print(flash_counter)