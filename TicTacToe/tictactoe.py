
def print_board(state):
    print("---------")
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(f"| {' '.join(row)} |")
    print("---------")

state = input("Enter cells: ")
print_board(state)
