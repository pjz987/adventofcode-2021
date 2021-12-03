filepath = 'day03/input.txt'
with open(filepath, 'r') as f:
    diagonostic = f.read().split('\n')

gamma_rate = ''
epsilon_rate = ''

tie_counter = 0

for i in range(len(diagonostic[0])):
    zeros = 0
    ones = 0
    for number in diagonostic:
        if number[i] == '0':
            zeros += 1
        elif number[i] == '1':
            ones += 1
    if zeros > ones:
        gamma_rate += '0'
        epsilon_rate += '1'
    elif ones > zeros:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        tie_counter += 1

if tie_counter:
    print(f'there were {tie_counter} ties')

gamma = 0
epsilon = 0

value = 1

for gamma_bit, epsilon_bit in zip(gamma_rate[::-1], epsilon_rate[::-1]):
    gamma += int(gamma_bit) * value
    epsilon += int(epsilon_bit) * value
    value *= 2

print(gamma * epsilon)