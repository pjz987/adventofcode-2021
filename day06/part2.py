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

lanternfish_list = list(map(lambda fish: int(fish), lanternfish))

lanternfish = {i: 0 for i in range(9)}
for fish in lanternfish_list:
    if fish not in lanternfish:
        lanternfish[fish] = 1
    else:
        lanternfish[fish] += 1



for _ in range(256):
    new_fish = lanternfish[0]
    for timer in range(8):
        lanternfish[timer] = lanternfish[timer + 1]
    lanternfish[6] += new_fish
    lanternfish[8] = new_fish

print(sum(lanternfish.values()))