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

    while True:
        first_player = input("Who will be the first (Name1, Name2): ")
        if first_player not in ["Name1", "Name2"]:
            print("Choose between 'Name1' and 'Name2'")
            continue
        break

    print("|" * pencils)
    print(f"{first_player} is going first!")
    return pencils, first_player


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


if __name__ == "__main__":
    pencils, current_player = initialize_game()

    while pencils > 0:
        pencils = player_turn(pencils, current_player)
        current_player = "Name1" if current_player == "Name2" else "Name2"

        if pencils == 0:
            print(f"{current_player} won!")
            break