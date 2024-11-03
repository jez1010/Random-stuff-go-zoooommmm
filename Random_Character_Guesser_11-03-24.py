import random
import string

def easy_generator():
    print("Easy Mode: Lowercase letters, total of 26 characters.")
    letters = string.ascii_lowercase
    print(list(letters))
    while True:
        b = random.randint(0,26)
        c = letters[b]
        d = input("What is your guess? (Type [end] to end the current session.) ")
        if c == d:
            print("You guessed the correct character!")
            break
        elif d.lower() == "end":
            break
        else:
            print("The character was " + c + "! You guessed wrong! Generating a new character...")
            pass

def medium_generator():
    print("Hard Mode: Uppercase and Lowercase letters, total of 52 characters.")
    letters = string.ascii_letters
    print(list(letters))
    while True:
        b = random.randint(0,51)
        c = letters[b]
        d = input("What is your guess? (Type [end] to end the current session.) ")
        if c == d:
            print("You guessed the correct character!")
            break
        elif d.lower() == "end":
            break
        else:
            print("The character was " + c + "! You guessed wrong! Generating a new character...")
            pass

def hard_generator():
    print("Hard Mode: Uppercase, Lowercase letters, and Number digits, total of 62 characters.")
    letters = string.ascii_letters + string.digits
    print(list(letters))
    while True:
        b = random.randint(0,61)
        c = letters[b]
        d = input("What is your guess? (Type [end] to end the current session.) ")
        if c == d:
            print("You guessed the correct character!")
            break
        elif d.lower() == "end":
            break
        else:
            print("The character was " + c + "! You guessed wrong! Generating a new character...")
            pass

def hardcore_generator():
    print("Hard Mode: Uppercase, Lowercase letters, Number digits, and Punctuation symbols, total of 96 characters.")
    letters = string.ascii_letters + string.digits + string.punctuation
    print(list(letters))
    while True:
        b = random.randint(0,96)
        c = letters[b]
        d = input("What is your guess? (Type [end] to end the current session.) ")
        if c == d:
            print("You guessed the correct character!")
            break
        elif d.lower() == "end":
            break
        else:
            print("The character was " + c + "! You guessed wrong! Generating a new character...")
            pass

def main():
    print("Random Character Guesser")
    while True:
        choose = input("Choose from easy [1], medium [2], hard[3], or hardcore[4]. Enter [end] to exit: ")
        if choose.lower() == "end":
            break
        elif choose == "1":
            easy_generator()
        elif choose == "2":
            medium_generator()
        elif choose == "3":
            hard_generator()
        elif choose == "4":
            hardcore_generator()
        else:
            print("Invalid format!")
            continue
    print("Session ended.")

if __name__ == "__main__":
    main()