import random
def function():
    while True:
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        b = random.randint(0,25)
        b = int(b)
        c = letters[b]
        d = input("What is your guess? ")
        if c == d:
            print("You guessed the correct letter!")
            break
        else:
            print("You guessed wrong! Generating a new letter...")
            continue

while True:
    print("Random Letter Guesser")
    function()
    e = True
    while e:
        f = input("Do you want to guess again? (yes/no)")
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
