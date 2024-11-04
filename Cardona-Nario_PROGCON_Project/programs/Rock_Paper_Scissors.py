import random
 
def numchecker(base):
    while True:
        try:
            int(base)
        except ValueError:
            print("Not an integer!")
            base = input("Reinput your base [0] [1] [2]: ")
            continue 
        else:
            return base 
def main():
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0
    rounds = 0
    while rounds < 3:
        computer = random.randint(0, 2)
        user = input("Enter 0 (Rock), 1 (Paper), or 2 (Scissors): ")
        user = numchecker(user)
        user = int(user)

 
        if user not in [0, 1, 2]:
            print("Invalid input. Please try again.")
            continue
        print(f"\nYou chose {choices[user]}, Computer chose {choices[computer]}.\n")
        if user == computer:
            print(f"Both chose {choices[computer]}! Tie!")
        elif (user == 0 and computer == 2) or \
             (user == 1 and computer == 0) or \
             (user == 2 and computer == 1):
            print(f"You win this round!")
            user_score += 1
        else:
            print(f"Computer wins this round.")
            computer_score += 1
        rounds += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")
    if user_score > computer_score:
        print("You win the game! Congratulations!")
    elif user_score < computer_score:
        print("Computer wins the game! Better luck next time!")
    else:
        print("It's a tie game!")
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__": #allows the main Hub py to import without running the code
    main()