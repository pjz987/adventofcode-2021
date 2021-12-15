filepath = 'day14/input.txt'
with open(filepath, 'r') as f:
    polymer_template, rules = f.read().split('\n\n')

# polymer_template, rules = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".split('\n\n')

pairs = dict(map(lambda rule: (rule.split(' -> ')[0], 0), rules.split('\n')))
print(pairs)
pairs_blank = pairs.copy()

occurences = dict(map(lambda char: (char, 0), list(set(polymer_template))))
print(occurences)

for pair in pairs:
    for char in pair:
        if char not in occurences:
            occurences[char] = 0
print(occurences)


for i, char in enumerate(polymer_template):
    if i == len(polymer_template) - 1:
        break
    pair = char + polymer_template[i + 1]
    pairs[pair] += 1

print(pairs)
rules = dict(map(lambda rule: (rule.split(' -> ')[0], rule.split(' -> ')[1]), rules.split('\n')))

for char in polymer_template:
    occurences[char] += 1
print(occurences)

def insert():
    global rules
    global occurences
    global pairs
    pairs_temp = pairs_blank.copy()
    for pair in pairs:
        # the value for this rules pair
        value = rules[pair]
        # the current value of the pair
        pairs_value = pairs[pair]
        # there will be as many new occurences for this value as there are pairs currently
        occurences[value] += pairs_value
        # the new triplet from the value inserted into that pair
        triplet = pair[0] + value + pair[1]
        # each half? of the triplet now appears once more for the pairs value
        pairs_temp[triplet[:2]] += pairs_value
        pairs_temp[triplet[1:]] += pairs_value
        pairs_temp[pair] -= pairs_value
    for pair in pairs_temp:
        pairs[pair] += pairs_temp[pair]

        

for _ in range(40):
    # print(polymer_template, '\n' + str(_))
    insert()
    print(occurences)

# print(occurences)

# set_chars = set(polymer_template)
# print(set_chars)

min_count = min(map(lambda char: occurences[char], occurences))
max_count = max(map(lambda char: occurences[char], occurences))

print(max_count - min_count)