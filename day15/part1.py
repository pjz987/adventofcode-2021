filepath = 'day15/input.txt'
with open(filepath, 'r') as f:
    lines = f.read().split('\n')

risk_map = [[int(risk) for risk in row] for row in lines]

start = (0, 0)
goal = (len(risk_map) - 1, len(risk_map[0]) - 1)

print(start, goal)

