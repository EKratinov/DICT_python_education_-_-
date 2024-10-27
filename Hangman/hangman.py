import random


def hangman_ver5():
        print("HANGMAN")
        words = ['python', 'java', 'javascript', 'php']
        word = random.choice(words)
        guessed = ['-' for _ in word]
        attempts_left = 8
        guessed_letters = set()

        while attempts_left > 0 and '-' in guessed:
            print(''.join(guessed))
            letter = input("Input a letter: > ").strip()

            if len(letter) != 1:
                print("You should input a single letter")
            elif not letter.islower():
                print("Please enter a lowercase English letter")
            elif letter in guessed_letters:
                print("You've already guessed this letter")
            elif letter in word:
                guessed_letters.add(letter)
                for i, l in enumerate(word):
                    if l == letter:
                        guessed[i] = letter
            else:
                guessed_letters.add(letter)
                attempts_left -= 1
                print("That letter doesn't appear in the word")

        if '-' not in guessed:
            print("You survived!")
        else:
            print("You lost!")


hangman_ver5()
