
def print_board(state):
    print("---------")
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(f"| {' '.join(row)} |")
    print("---------")


def analyze_game(state):
    def check_winner(symbol):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # verticals
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
        return any(all(state[pos] == symbol for pos in pattern) for pattern in win_patterns)

    if abs(state.count("X") - state.count("O")) > 1:
        return "Impossible"
    if check_winner("X") and check_winner("O"):
        return "Impossible"
    if check_winner("X"):
        return "X wins"
    if check_winner("O"):
        return "O wins"
    if "_" in state:
        return "Game not finished"
    return "Draw"


state = input("Enter cells: ")
print_board(state)
print(analyze_game(state))