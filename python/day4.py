n = 5

with open("../inputs/day4.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

draws = [int(x) for x in lines[0].split(",")]


def load_boards():
    boards = []
    for i in range(1, len(lines) - 1, n + 1):
        board = []
        for j in range(1, n + 1):
            row = [int(x) for x in lines[i + j].split()]
            board.append(row)
        boards.append(board)
    return boards


boards = load_boards()

winner = None
for draw in draws:
    for board in boards:
        for i in range(n):
            for j in range(n):
                if board[i][j] == draw:
                    board[i][j] = None

                    row_win = all(board[i][k] is None for k in range(5))
                    col_win = all(board[k][j] is None for k in range(5))
                    if row_win or col_win:
                        winner = board
    if winner:
        break

_sum = sum(winner[i][j] for i in range(n) for j in range(n) if winner[i][j])
print(f"part one: {draw * _sum}")

# reset boards for part two
boards = load_boards()

remaining_boards = set(range(len(boards)))
draw_num = 0
while len(remaining_boards) > 0:
    draw = draws[draw_num]
    draw_num += 1

    tmp = set()

    for board_num in remaining_boards:
        board = boards[board_num]

        winner = False
        for i in range(n):
            for j in range(n):
                if board[i][j] == draw:
                    board[i][j] = None

                    row_win = all(board[i][k] is None for k in range(5))
                    col_win = all(board[k][j] is None for k in range(5))
                    winner = row_win or col_win

        if not winner:
            tmp.add(board_num)

    remaining_boards = tmp

loser = board
_sum = sum(loser[i][j] for i in range(n) for j in range(n) if loser[i][j])
print(f"part two: {draw * _sum}")
