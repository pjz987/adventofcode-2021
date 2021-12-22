filepath = 'day16/input.txt'
with open(filepath, 'r') as f:
    raw_hex = f.read()

hex_to_bits = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

bits_to_hex = {val: key for key, val in hex_to_bits.items()}

# 1. convert hex to bits
bits = ''.join(map(lambda hex_num: hex_to_bits[hex_num], raw_hex))
# 2. get version
version = bits[:3]
# 3. get type id
type_id = bits[3:6] # 100 or 4: a single binary number
