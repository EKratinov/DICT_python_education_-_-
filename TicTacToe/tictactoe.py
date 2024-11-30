def print_board(state):
    print("---------")
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(f"| {' '.join(row)} |")
    print("---------")


def analyze_game(state):
    def check_winner(symbol):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
            [0, 4, 8], [2, 4, 6]              # диагонали
        ]
        return any(all(state[pos] == symbol for pos in pattern) for pattern in win_patterns)

    if check_winner("X"):
        return "X wins"
    if check_winner("O"):
        return "O wins"
    if "_" not in state:
        return "Draw"
    return "Game not finished"


def make_move(state, player):
    while True:
        try:
            coords = input(f"Enter the coordinates for {player}: ").split()
            if len(coords) != 2 or not all(c.isdigit() for c in coords):
                raise ValueError("You should enter numbers!")

            x, y = map(int, coords)
            if not (1 <= x <= 3 and 1 <= y <= 3):
                raise ValueError("Coordinates should be from 1 to 3!")


            index = (y - 1) * 3 + (x - 1)
            if state[index] != "_":
                raise ValueError("This cell is occupied! Choose another one!")
            state = state[:index] + player + state[index + 1:]
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

