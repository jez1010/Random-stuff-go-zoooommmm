import random
 

words = ["internet", "monitor", "mobile", "projector", "aircon"]
def main():
    hearts = 5
    rounds = 3
    score = 0
    a = 1 # display the amount of rounds
    while hearts != 0 and a < 4:
        word = random.choice(words)
        word_length = len(word)
        display = ["_"] * word_length
        guessed = False
        guessed_letters = []
        guessed_words = []
        hints = 3
        print(f"Round {a}")
        print(" ".join(display))
        print(f"Hearts: {hearts}")
        a = a + 1 #display the addition of every rounds
        while not guessed and hearts > 0:
            guess = input("Guess the hidden letter or word: ").lower()
            if len(guess) == 1 and guess.isalpha(): #if input is a letter
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    hearts -= 1
                    guessed_letters.append(guess)
                    if hints > 0:
                        hints -= 1
                        print(f"Hints left: {hints}")
                        print(f"Hint: {word[random.randint(0, word_length-1)]}")
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word)
                    indices = [i for i, letter in enumerate(word_as_list) if letter == guess]
                    for index in indices:
                        display[index] = guess
            elif len(guess) == word_length and guess.isalpha(): #if input is a word
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    hearts -= 1
                    guessed_words.append(guess)
                    if hints > 0:
                        hints -= 1
                        print(f"Hints left: {hints}")
                        print(f"Hint: {word[random.randint(0, word_length-1)]}")
                else:
                    guessed = True
                    display = list(guess)
            else:
                print("Invalid guess.")
            print(" ".join(display))
            print(f"Hearts: {hearts}")
        if guessed:
            print("Congratulations, you guessed the word!")
            score += 1
        else:
            print(f"Sorry guess not enough, the word was {word}.")
            rounds = 0
    a = 3
    print(f"Your final score is {score} out of {a}.")

if __name__ == "__main__": #allows the main Hub py to import without running the code 
    main()
