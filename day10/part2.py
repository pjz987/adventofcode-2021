filepath = 'day10/input.txt'
with open(filepath, 'r') as f:
    lines = f.read().split('\n')

opening = '([{<'
closing = ')]}>'

character_matcher = dict(zip(closing, opening))

opening_to_closing = dict(zip(opening, closing))


character_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

for i, line in enumerate(lines):
    stack = []
    for character in line:
        if character in opening:
            stack.append(character)
        else:
            if character_matcher[character] == stack[-1]:
                stack.pop()
            else:
                lines[i] = None
                break

autocomplete_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

lines = list(filter(lambda line: line is not None, lines))
def compute_score(completion_list):
    score = 0
    for character in completion_list:
        score *= 5
        score += autocomplete_table[character]
    return score
    

autocomplete_scores = []

for line in lines:
    stack = []
    for character in line:
        if character in opening:
            stack.append(character)
        else:
            stack.pop()
    stack.reverse()
    completion_list = list(map(lambda character: opening_to_closing[character], stack))
    autocomplete_scores.append(compute_score(completion_list))

from math import floor
autocomplete_scores.sort()
print(autocomplete_scores[floor(len(autocomplete_scores) / 2)])

