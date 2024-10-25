import random
import string
def function():
    while True:
        letters = string.ascii_letters
        b = random.randint(0,51)
        c = letters[b]
        d = input("What is your guess? (Type 'End' to end the game.) ")
        if c == d:
            print("You guessed the correct letter!")
            break
        elif d == "end" or d == "end" or d == "END":
            g = "break"
            break
        else:
            print("The letter was " + c + "! You guessed wrong! Generating a new letter...")
            continue

while True:
    print("Random Letter Guesser")
    function()
    e = True
    while e:
        f = input("Do you want to guess again? (yes/no) ")
        if f == "yes":
            e = False
            continue
        elif f == "no":
            break
        else:
            print("ERROR: Not a valid input")
            continue
    if f == "no": break

print("End of session.")
