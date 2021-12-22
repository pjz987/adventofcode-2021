# target area: x=20..30, y=-10..-5

target_area = {
    'x': range(20, 31),
    'y': range(-10, -4),
}

class Probe:
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.in_target = {
            'x': None,
            'y': None
        }
        self.max_y = y
    
    def turn(self):
        self.x += self.vx
        self.y += self.vy
        self.max_y = self.y if self.y > self.max_y else self.max_y
        if self.vx:
            self.vx += 1 if self.vx < 0 else -1
        self.vy -= 1
        last_in_target = self.in_target
        self.in_target = self.check_target()
        # print('-'*40)
        # print(self.in_target)
        # print(last_in_target)
        # print(self.x, self.y)
        if set(self.in_target.values()) == { 0 }:
            return 'hit', None
        if last_in_target['x'] == -1 and self.in_target['x'] == 1:
            return 'overshot', 'x'
        if last_in_target['y'] == 1 and self.in_target['y'] == -1:
            return 'overshot', 'y'
        if self.vx == 0 and self.in_target['x'] != 0:
            return 'stalled', 'x'
        if self.vx == 0 and self.in_target['y'] == -1:
            return 'stalled', 'x'
        return 'continue', None
    
    def check_target(self):
        global target_area
        if self.x in target_area['x']:
            x = 0
        else:
            x = -1 if self.x < min(target_area['x']) else 1
        if self.y in target_area['y']:
            y = 0
        else:
            y = -1 if self.y < min(target_area['y']) else 1
        return {'x': x, 'y': y}

max_ys = []

def run_simulation(x=0, y=0):
    global max_ys
    probe = Probe(vx=x, vy=y)
    while True:
        result, axis = probe.turn()
        if result == 'hit':
            max_ys.append(probe.max_y)
            print(max_ys)
            return probe, result, axis
        if result == 'overshot':
            return probe, result, axis
try:
    for x in range(1, 31):
        y = 0
        while True:
            y += 1
            print(x, y)
            probe, result, axis = run_simulation(x, y)
            if result == 'stalled':
                break
        if result == 'overshot':
            break
except KeyboardInterrupt:
    print(x, y)

print(max(max_ys))