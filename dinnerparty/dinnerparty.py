

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
    return friends


friends, num_of_friends = add_friends()
friends = split_bill(friends, num_of_friends)