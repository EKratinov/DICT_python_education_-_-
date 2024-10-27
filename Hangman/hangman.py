import random


def hangman_ver2():
    print("HANGMAN")
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    guess = input("Guess the word: > ").strip().lower()
    if guess == word:
        print("You survived!")
    else:
        print("You lost!")


hangman_ver2()
