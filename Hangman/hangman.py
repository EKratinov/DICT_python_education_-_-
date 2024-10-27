import random


def hangman_ver3():
    print("HANGMAN")
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hint = word[:3] + '-' * (len(word) - 3)
    print(f"Guess the word {hint}: > ", end="")
    guess = input().strip().lower()
    if guess == word:
        print("You survived!")
    else:
        print("You lost!")


hangman_ver3()
