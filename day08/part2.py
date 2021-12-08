filepath = 'day08/input.txt'
with open(filepath, 'r') as f:
    signals = f.read().split('\n')

signals = list(map(lambda line: line.split(' | '), signals))
for i, signal in enumerate(signals):
    signals[i] = list(map(lambda data: data.split(), signals[i]))

num_to_segments = {
    # 1: 2,
    # 7: 3,
    # 4: 4,
    # 2: 5,
    # 3: 5,
    # 5: 5,
    # 0: 6,
    # 6: 6,
    # 9: 6,
    # 8: 7,
}

empty_decoder = {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
}

def three_from_one(one, wires_len5):
    for wire in wires_len5:
        if one[0] in wire and one[1] in wire:
            return wire

def nine_from_three(three, wires_len6):
    for wire in wires_len6:
        flag = True
        for letter in three:
            if letter not in wire:
                flag = False
                break
        if flag:
            return wire

def zero_from_one(one, wires_len6):
    for wire in wires_len6:
        if one[0] in wire and one[1] in wire:
            return wire

def five_from_six(six, wires_len_5):
    for wire in wires_len_5:
        flag = True
        for letter in wire:
            if letter not in six:
                flag = False
                break
        if flag:
            return wire

def signal_decoder(wires, decoder=empty_decoder.copy()):
    for wire in wires:
        if len(wire) == 2:
            decoder[1] = wire
        elif len(wire) == 4:
            decoder[4] = wire
        elif len(wire) == 3:
            decoder[7] = wire
        elif len(wire) == 7:
            decoder[8] = wire
    wires_len5 = list(filter(lambda wire: len(wire) == 5, wires))
    wires_len6 = list(filter(lambda wire: len(wire) == 6, wires))
    decoder[3] = three_from_one(decoder[1], wires_len5)
    wires_len5.pop(wires_len5.index(decoder[3]))
    decoder[9] = nine_from_three(decoder[3], wires_len6)
    wires_len6.pop(wires_len6.index(decoder[9]))
    decoder[0] = zero_from_one(decoder[1], wires_len6)
    wires_len6.pop(wires_len6.index(decoder[0]))
    decoder[6] = wires_len6[0]
    decoder[5] = five_from_six(decoder[6], wires_len5)
    wires_len5.pop(wires_len5.index(decoder[5]))
    decoder[2] = wires_len5[0]

    return decoder

# print(signal_decoder('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split()))

total = 0

for signal in signals:
    wires, digits = signal
    decoder = signal_decoder(wires)
    decoder = {''.join(sorted(list(v))): str(k) for k, v in decoder.items()}
    # print(decoder)
    number = ''
    for digit in digits:
        number += decoder[''.join(sorted(list(digit)))]
    
    total += int(number)

print(total)
