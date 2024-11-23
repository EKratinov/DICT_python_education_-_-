import random


def get_number_of_friends():
    while True:
        try:
            num_of_people = int(input("Enter the number of friends joining (including you): "))
            if num_of_people <= 0:
                print("No one is joining for the party")
                return 0
            return num_of_people
        except ValueError:
            print("Please enter a valid number.")


def add_friends():
    num_of_friends = get_number_of_friends()
    if num_of_friends == 0:
        return {}, 0

    friends_dict = {}
    for _ in range(num_of_friends):
        name = input("Enter the name of every friend (including you), each on a new line: ").strip()
        friends_dict[name] = 0
    print("Friends list:", friends_dict)
    return friends_dict, num_of_friends


def split_bill(friends_dict, num_friends):
    if total_friends > 0:
        while True:
            try:
                total_bill = float(input("Enter the total amount: "))
                break
            except ValueError:
                print("Please enter a number.")
        split_amount = round(total_bill / num_friends, 2)
        for friend in friends_dict:
            friends_dict[friend] = split_amount
        print("Updated friends list with split amounts:", friends_dict)
        return friends_dict, total_bill
    return friends_dict, 0


def choose_lucky(friends_dict):
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ').strip()
    if lucky_choice.lower() == "yes":
        lucky_person = random.choice(list(friends_dict.keys()))
        print(f"{lucky_person} is the lucky one!")
        return lucky_person
    else:
        print("No one is going to be lucky")
        return None


def recalculate_bill(friends_dict, lucky_friend, bill_amount):
    if lucky_friend:
        new_split_amount = round(bill_amount / (len(friends_dict) - 1), 2)
        for friend in friends_dict:
            friends_dict[friend] = new_split_amount if friend != lucky_person else 0
    print("Final friends list with recalculated amounts:", friends_dict)
    return friends_dict


friends, total_friends = add_friends()
if total_friends > 0:
    friends, total_bill = split_bill(friends, total_friends)
    lucky_person = choose_lucky(friends)
    friends = recalculate_bill(friends, lucky_person, total_bill)
