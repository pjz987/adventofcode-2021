filepath = 'day03/input.txt'
with open(filepath, 'r') as f:
    diagonostic = f.read().split('\n')

# diagonostic = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".split('\n')

def get_most_least_common_bit(data, pos, most_or_least):
    zeros = 0
    ones = 0
    for number in data:
        if number[pos] == '0':
            zeros += 1
        elif number[pos] == '1':
            ones += 1
    if most_or_least == 'most':
        if zeros == ones:
            return '1'
        return '0' if zeros > ones else '1'
    if most_or_least == 'least':
        if zeros == ones:
            return '0'
        return '1' if zeros > ones else '0'

def bit_criteria_filter(number, pos, bit):
    return True if number[pos] == bit else False

def run_bit_criteria_filter(data, pos, bit):
    return list(filter(lambda number :
            bit_criteria_filter(number, pos, bit),
            data))

def binary_to_decimal(binary):
    bit_value = 1
    decimal = 0
    for bit in binary[::-1]:
        decimal += int(bit) * bit_value
        bit_value *= 2
    return decimal

oxygen_data = diagonostic.copy()
co2_data = diagonostic.copy()

for pos in range(len(diagonostic[0])):
    print('O2 ', oxygen_data)
    if len(oxygen_data) > 1:
        mcb = get_most_least_common_bit(oxygen_data, pos, 'most')
        oxygen_data = run_bit_criteria_filter(oxygen_data, pos, mcb)
    print('O2 ', oxygen_data)
    
    print('CO2',co2_data)
    if len(co2_data) > 1:
        lcb = get_most_least_common_bit(co2_data, pos, 'least')
        co2_data = run_bit_criteria_filter(co2_data, pos, lcb)
    print('CO2',co2_data)
    
    print('-'*80)
    
#     # print(len(oxygen_data), len(co2_data))

# print(oxygen_data, co2_data)

oxygen_rating = binary_to_decimal(oxygen_data[0])
co2_rating = binary_to_decimal(co2_data[0])
print(oxygen_rating, co2_rating)
life_support_rating = oxygen_rating * co2_rating
print(life_support_rating)