def print_fixed_board():
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "X", "O"]
    ]
    for row in board:
        print(" ".join(row))

print_fixed_board()