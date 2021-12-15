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

rules = dict(map(lambda rule: (rule.split(' -> ')[0], rule.split(' -> ')[1]), rules.split('\n')))

def insert(template):
    global rules
    insertion_index = None
    template = list(template)
    for i, character in enumerate(template):
        if i == len(template) - 1:
            break
        if insertion_index is not None and i <= insertion_index:
            continue
        next_char = template[i + 1]
        pair = character + next_char
        if pair in rules:
            template.insert(i + 1, rules[pair])
            insertion_index = i + 1
    return ''.join(template)
    # for pair, element in rules.items():
    #     template = template.replace(pair, pair[0] + element + pair[1])
    # return template

for _ in range(10):
    print(polymer_template, '\n' + str(_))
    polymer_template = insert(polymer_template)

set_chars = set(polymer_template)
print(set_chars)

min_count = min(map(lambda char: polymer_template.count(char), polymer_template))
max_count = max(map(lambda char: polymer_template.count(char), polymer_template))

print(max_count - min_count)