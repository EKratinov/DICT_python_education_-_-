import random


def add_friends():
    num_of_friends = int(input("Enter the number of friends joining (including you): "))
    if num_of_friends <= 0:
        print("No one is joining for the party")
        return {}, 0
    else:
        friends = {}
        for _ in range(num_of_friends):
            name = input("Enter the name of every friend (including you), each on a new line: ")
            friends[name] = 0
        print("Friends list:", friends)
        return friends, num_of_friends


def split_bill(friends, num_of_friends):
    if num_of_friends > 0:
        total_amount = float(input("Enter the total amount: "))
        split_amount = round(total_amount / num_of_friends, 2)
        for friend in friends:
            friends[friend] = split_amount
        print("Updated friends list with split amounts:", friends)
    return friends, total_amount
    return friends, 0


def choose_lucky(friends):
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if lucky_choice in ["Yes", "yes", "yes ", "Yes "]:
        lucky_friend = random.choice(list(friends.keys()))
        print(f"{lucky_friend} is the lucky one!")
        return lucky_friend
    else:
        print("No one is going to be lucky")
        return None


def recalculate(friends, lucky_friend, total_amount):
    if lucky_friend:
        new_split_amount = round(total_amount / (len(friends) - 1), 2)
        for friend in friends:
            friends[friend] = new_split_amount if friend != lucky_friend else 0
    print("Final friends list with recalculated amounts:", friends)
    return friends


friends, num_of_friends = add_friends()
friends, total_amount = split_bill(friends, num_of_friends)
lucky_friend = choose_lucky(friends)
friends = recalculate(friends, lucky_friend, total_amount)
