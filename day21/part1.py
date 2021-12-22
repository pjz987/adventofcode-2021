class DeterministicDie:
    def __init__(self):
        self.number = 0
        self.times_rolled = 0
    
    def roll(self):
        if self.number == 100:
            self.number = 0
        self.number += 1
        self.times_rolled += 1
        return self.number

class Player:
    def __init__(self, starting_position):
        self.position = starting_position
        self.score = 0
    
    def turn(self, die: DeterministicDie):
        for _ in range(3):
            self.position += die.roll()
        if self.position > 10:
            self.position = self.position % 10
            if self.position == 0:
                self.position = 10
        self.score += self.position

players = [Player(4), Player(2)]
# players = [Player(4), Player(8)]
die = DeterministicDie()
i = 0
while True:
    player = players[i % 2]
    player.turn(die)
    if player.score >= 1000:
        break
    i += 1

i += 1
losing_player = players[i % 2]
print(player.score, losing_player.score)
print(losing_player.score * die.times_rolled)