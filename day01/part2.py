file_path = 'day01/input.txt'
with open(file_path, 'r') as file:
    measurements = file.read().split('\n')

measurements = list(map(lambda x: int(x), measurements))
print(measurements)

increase_counter = 0
last_sum = None

for i in range(len(measurements)):
    if i <= 1: continue
    this_sum = sum(measurements[i-3:i])
    if last_sum is not None:
        if this_sum > last_sum:
            increase_counter += 1
    last_sum = this_sum

print(increase_counter)