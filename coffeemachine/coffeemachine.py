water, milk, coffee_beans, cups, money = 400, 540, 120, 9, 550


def print_status():
    print("\nThe coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")


def buy():
    global water, milk, coffee_beans, cups, money
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choice == "back":
        return
    if choice == "1":  # Espresso
        needed_water, needed_milk, needed_beans, cost = 250, 0, 16, 4
    elif choice == "2":  # Latte
        needed_water, needed_milk, needed_beans, cost = 350, 75, 20, 7
    elif choice == "3":  # Cappuccino
        needed_water, needed_milk, needed_beans, cost = 200, 100, 12, 6
    else:
        print("Invalid option.")
        return


    if water < needed_water:
        print("Sorry, not enough water!")
    elif milk < needed_milk:
        print("Sorry, not enough milk!")
    elif coffee_beans < needed_beans:
        print("Sorry, not enough coffee beans!")
    elif cups < 1:
        print("Sorry, not enough disposable cups!")
    else:
        water -= needed_water
        milk -= needed_milk
        coffee_beans -= needed_beans
        cups -= 1
        money += cost
        print("I have enough resources, making you a coffee!")


def fill():
    global water, milk, coffee_beans, cups
    water += int(input("Write how many ml of water you want to add: "))
    milk += int(input("Write how many ml of milk you want to add: "))
    coffee_beans += int(input("Write how many grams of coffee beans you want to add: "))
    cups += int(input("Write how many disposable coffee cups you want to add: "))


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_status()
    elif action == "exit":
        break
    else:
        print("Invalid action.")
