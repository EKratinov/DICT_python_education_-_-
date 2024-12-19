# Etap 1: Initialize the game
# Define a function to get the number of pencils and the first player
def initialize_game():
    while True:
        pencils = input("How many pencils would you like to use: ")
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils)
        if pencils <= 0:
            print("The number of pencils should be positive")
            continue
        break

    player1 = input("Enter the name of the first player: ")
    player2 = input("Enter the name of the second player: ")

    while True:
        first_player = input(f"Who will be the first ({player1}, {player2}): ")
        if first_player not in [player1, player2]:
            print(f"Choose between '{player1}' and '{player2}'")
            continue
        break

    print("|" * pencils)
    print(f"{first_player} is going first!")
    return pencils, first_player, player1, player2

# Etap 2: Player turns
# Define a function to handle player turns
def player_turn(pencils, current_player):
    while True:
        print(f"{current_player}'s turn!")
        move = input("> ")
        if not move.isdigit() or int(move) not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
            continue
        move = int(move)
        if move > pencils:
            print("Too many pencils were taken")
            continue
        break

    pencils -= move
    print("|" * pencils)
    return pencils

# Etap 3: Error handling and winner declaration
# Extend the game logic to determine and announce the winner
def declare_winner(pencils, current_player):
    if pencils == 0:
        print(f"{current_player} won!")

# Etap 4: Add a bot to the game
# Define a function for bot moves with a winning strategy
def bot_turn(pencils):
    if pencils % 4 == 0:
        move = 3
    elif pencils % 4 == 3:
        move = 2
    elif pencils % 4 == 2:
        move = 1
    else:
        move = 1

    print(f"{player2} turn: {move}")
    pencils -= move
    print("|" * pencils)
    return pencils

# Example of execution for Etap 4
if __name__ == "__main__":
    pencils, current_player, player1, player2 = initialize_game()

    while pencils > 0:
        if current_player == player1:
            pencils = player_turn(pencils, current_player)
            current_player = player2
        else:
            pencils = bot_turn(pencils)
            current_player = player1

        if pencils == 0:
            declare_winner(pencils, current_player)
            break
