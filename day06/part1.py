filepath = 'day06/input.txt'
with open (filepath, 'r') as f:
    lanternfish = f.read().split(',')

# lanternfish = '3,4,3,1,2'.split(',')

class Lanternfish:
    def __init__(self, internal_timer):
        self.internal_timer = internal_timer
    
    def day_passes(self):
        if self.internal_timer == 0:
            self.internal_timer = 6
            return True
        self.internal_timer -= 1
    
    def __str__(self) -> str:
        return str(self.internal_timer)

lanternfish = list(map(lambda fish: Lanternfish(int(fish)), lanternfish))

def pass_day_for_fish(fish):
    global lanternfish
    global new_fish_count
    if fish.day_passes():
        new_fish_count += 1
    return fish
new_fish_count = 0
for _ in range(80):
    print(_, len(lanternfish), new_fish_count)
    new_fish_count = 0  
    lanternfish = list(map(pass_day_for_fish, lanternfish))
    for _ in range(new_fish_count):
        lanternfish.append(Lanternfish(8))
    # for fish in lanternfish:
    #     if fish.day_passes():
    #         new_fish += 1
    # for _ in range(new_fish):
    #     lanternfish.append(Lanternfish(8))

print(len(lanternfish))