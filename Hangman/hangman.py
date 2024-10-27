import random


def hangman_ver4():
    print("HANGMAN")
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    guessed = ['-' for _ in word]
    attempts = 8

    while attempts > 0 and '-' in guessed:
        print(''.join(guessed))
        letter = input("Input a letter: > ").strip().lower()

        if letter in word:
            for i, l in enumerate(word):
                if l == letter:
                    guessed[i] = letter
        else:
            attempts -= 1
            print("That letter doesn't appear in the word")

        if '-' not in guessed:
            print("You survived!")
            return
    print("You lost!")


hangman_ver4()
