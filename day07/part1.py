filepath = 'day07/input.txt'
with open(filepath, 'r') as f:
    crabs = list(map(lambda crab: int(crab), f.read().split(',')))

# crabs = list(map(lambda crab: int(crab), '16,1,2,0,4,2,7,1,2,14'.split(',')))

print(crabs)
print(len(crabs), min(crabs), max(crabs))
print(sum(crabs) / len(crabs))

total_movements = []

for pos in range(min(crabs), max(crabs)):
    total_movement = 0
    for crab in crabs:
        total_movement += abs(crab - pos)
    total_movements.append(total_movement)

print(min(total_movements))