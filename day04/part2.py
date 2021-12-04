filepath = 'day04/input.txt'
with open(filepath, 'r') as f:
    contents = f.read().split('\n\n')

numbers = contents[0].split(',')
boards = list(map(lambda board:
         board.split('\n'), contents[1:]))
boards = [
    {
        'won': False,
        'board': list(map(lambda board: board.split(), board)),
    } for board in boards]

def sum_of_board(board):
    total = 0
    for row in board:
        for number in row:
            if number is not None:
                total += int(number)
    return total

def check_number(called_number, board):
    for row in board:
        for i, number in enumerate(row):
            if number == called_number:
                row[i] = None

    for row in board:
        if set(row) == {None}:
            return 'Bingo!'
    for i in range(len(board)):
        column = [board[i][j] for j in range(len(board))]
        if set(column) == {None}:
            return 'Bingo!'

winners = []

def play_bingo():
    global numbers
    global board
    global winners
    winning_number = None
    for number in numbers:
        for board in boards:
            if not board['won']:
                if check_number(number, board['board']) == 'Bingo!':
                    winning_number = number
                    board['won'] = True
                    winners.append(board)
    print(int(winning_number) * sum_of_board(winners[-1]['board']))

play_bingo()
