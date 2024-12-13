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


if __name__ == "__main__":
    pencils, current_player = initialize_game()
