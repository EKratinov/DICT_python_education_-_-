def hangman_ver1():
    print("HANGMAN")
    word = "python"
    guess = input("Guess the word: > ").strip().lower()
    if guess == word:
        print("You survived!")
    else:
        print("You lost!")


hangman_ver1()
