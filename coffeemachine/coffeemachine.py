water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups = int(input("Write how many cups of coffee you will need: "))


required_water = cups * 200
required_milk = cups * 50
required_coffee_beans = cups * 15


if water > 0 and milk > 0 and coffee_beans > 0:
    max_cups_water = water // 200
    max_cups_milk = milk // 50
    max_cups_beans = coffee_beans // 15


    max_possible_cups = min(max_cups_water, max_cups_milk, max_cups_beans)

    
    if max_possible_cups >= cups:
        extra_cups = max_possible_cups - cups
        if extra_cups > 0:
            print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
        else:
            print("Yes, I can make that amount of coffee")
    else:
        print(f"No, I can make only {max_possible_cups} cups of coffee")
else:
    print("No, I can make only 0 cups of coffee")
