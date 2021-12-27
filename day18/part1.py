from math import ceil, floor

filepath = 'day18/input.txt'
with open(filepath, 'r') as f:
    numbers = list(map(lambda number: eval(number), f.read().split('\n')))

print(numbers)

def explode(number, depth=0):
    for value in number:
        if type(value) is list:
            ...