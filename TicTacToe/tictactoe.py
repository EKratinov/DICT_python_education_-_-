def print_board(state):
    print("---------")
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(f"| {' '.join(row)} |")
    print("---------")


def analyze_game(state):
    def check_winner(symbol):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
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


def make_move(state, current_player):
    while True:
        try:
            coords = input(f"Enter the coordinates for {current_player}: ").split()
            if len(coords) != 2 or not all(c.isdigit() for c in coords):
                raise ValueError("You should enter numbers!")

            x, y = map(int, coords)
            if not (1 <= x <= 3 and 1 <= y <= 3):
                raise ValueError("Coordinates should be from 1 to 3!")

            index = (x - 1) * 3 + (y - 1)
            if state[index] != "_":
                raise ValueError("This cell is occupied! Choose another one!")

            state = state[:index] + current_player + state[index + 1:]
            return state
        except ValueError as e:
            print(e)


def tic_tac_toe():
    state = "_________"
    print_board(state)
    current_player = "X"

    while True:
        state = make_move(state, current_player)
        print_board(state)

        result = analyze_game(state)
        if result != "Game not finished":
            print(result)
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
