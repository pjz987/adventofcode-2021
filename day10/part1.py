filepath = 'day10/input.txt'
with open(filepath, 'r') as f:
    lines = f.read().split('\n')

print(lines)
opening = '([{<'
closing = ')]}>'

character_matcher = dict(zip(closing, opening))

illegal_character_counter = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0,
}

character_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

for line in lines:
    stack = []
    for character in line:
        if character in opening:
            stack.append(character)
        else:
            if character_matcher[character] == stack[-1]:
                stack.pop()
            else:
                illegal_character_counter[character] += 1
                break

syntax_error_score = sum(map(lambda character:
    illegal_character_counter[character] * character_points[character], closing))

print(syntax_error_score)
