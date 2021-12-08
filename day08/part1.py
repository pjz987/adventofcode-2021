filepath = 'day08/input.txt'
with open(filepath, 'r') as f:
    signals = f.read().split('\n')

signals = list(map(lambda line: line.split(' | '), signals))
print(signals)

counter = 0

for signal in signals:
    print(signal[1].split())
    for digit in signal[1].split(' '):
        # print(len(digit) in (2, 4, 3, 7))
        if len(digit) in (2, 4, 3, 7):
            counter += 1

print(counter)