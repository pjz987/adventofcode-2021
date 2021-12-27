from math import ceil, floor

filepath = 'day24/input.txt'
with open(filepath, 'r') as f:
    instructions = f.read().split('\n')

nested_instructions = []
input_indices = []

for i, instruction in enumerate(instructions):
    if 'inp' in instruction:
        input_indices.append(i)

for i, index in enumerate(input_indices):
    if i < len(input_indices) - 1:
        next_index = input_indices[i + 1]
        nested_instructions.append(instructions[index:next_index])

def inp(a=9):
    global model_number
    model_number.append(str(a))
    return a

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    a = a / b
    if a > 0:
        return floor(a)
    if a < 0:
        return ceil(a)
    return 0

def mod(a, b):
    if a < 0 or b <= 0:
        raise ZeroDivisionError
    return a % b

def eql(a, b):
    return 1 if a == b else 0

def set_result(a, result, w, x, y, z):
    if a == 'w':
        w = result
    elif a == 'x':
        x = result
    elif a == 'y':
        y = result
    elif a == 'z':
        z = result
    return w, x, y, z

def arithmetic_logic_unit(instruction: str, inp: int, w=0, x=0, y=0, z=0):
    instruction = instruction.split()
    if len(instruction) == 2:
        _, a = instruction
        result = inp

    else:
        opr, a, b = instruction
        result = eval(f'{opr}({a},{b})')
    w, x, y, z = set_result(a, result, w, x, y, z)
    return w, x, y, z


class ModelNumberAccumulator:
    def __init__(self):
        self.w, self.x, self.y, self.z = 0, 0, 0, 0
        self.model_numbers = [9] * 14
    
    def reduce_model_numbers(self):
        for i in range(len(self.model_numbers) - 1, 0, -1):
            number = self.model_numbers[i]
            if number > 1:
                self.model_numbers[i] -= 1
                return
    
    def accumulate(self, i=0):
        global nested_instructions
        if i == len(nested_instructions):
            if self.z == 0:
                return True
            return False
            self.model_numbers = reduce_model_numbers(self.model_numbers)

        instructions = nested_instructions[i]
        inp = self.model_numbers[i]
        try:
            for instruction in instructions:
                self.w, self.x, self.y, self.z = arithmetic_logic_unit(
                    instruction, inp, self.w, self.x, self.y, self.z
                )
        except ZeroDivisionError:
            inp -= 1
            self.model_numbers.pop()
            if inp <= 0:
                i -= 1
            return self.accumulate(i, inp)
        i += 1
        return self.accumulate(i)

model_number = []



# w, x, y, z = 0, 0, 0, 0
# for instruction in instructions:
#     w, x, y, z = arithmetic_logic_unit(instruction, w, x, y, z)
#     print(w, x, y, z)

# print(model_number)

mda = ModelNumberAccumulator()
while True:
    done = mda.accumulate()
    if done:
        break
    mda.reduce_model_numbers()

print(mda.model_numbers)