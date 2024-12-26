class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550


    def print_status(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


    def buy(self):
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


        if self.water < needed_water:
            print("Sorry, not enough water!")
        elif self.milk < needed_milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < needed_beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.water -= needed_water
            self.milk -= needed_milk
            self.coffee_beans -= needed_beans
            self.cups -= 1
            self.money += cost
            print("I have enough resources, making you a coffee!")


    def fill(self):
        self.water += int(input("Write how many ml of water you want to add: "))
        self.milk += int(input("Write how many ml of milk you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add: "))
        self.cups += int(input("Write how many disposable coffee cups you want to add: "))


    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


    def process_input(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.print_status()
        elif action == "exit":
            return False
        else:
            print("Invalid action.")
        return True


machine = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if not machine.process_input(action):
        break
