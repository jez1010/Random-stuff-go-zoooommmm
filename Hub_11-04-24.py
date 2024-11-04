import os
import sys

def choicechecker(choice): # Checks if choice is a number, if not it asks you to reinput, also checks if it is within the choices
    while True:
        try:
            int(choice)
        except ValueError:
            print("Not an integer!")
            choice = input("Reinput your choice [1] [2] [3] [4] [5]: ") 
            continue 
        else:
            return choice

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'programs')) # directory thing (i do not understand)

def main():
    while True:
        print("\nChoose an option:")
        print("Educational Tools:\n[1] Number System Converter\n[2] Random Character Guesser\n\nMinigames:\n[3] Random Character Guesser\n[4] Rock Paper Scissors\n[5] Hangman\n\nType 'end' to end the program")
        
        choice = input("Enter your choice. Press 'end' to exit: ").strip()
        choice = choicechecker(choice)
        

        if choice == "1":
            import Number_System_Converter
            Number_System_Converter.main()
        elif choice == "2":
            import Number_System_Calculator
            Number_System_Calculator.main()
        elif choice == "3":
            import Random_Character_Guesser
            Random_Character_Guesser.main()
        elif choice == "4":
            import Rock_Paper_Scissors
            Rock_Paper_Scissors.main()
        elif choice == "5":
            import Hangman
            Hangman.main()
        elif choice.lower() == "end":
            print("Session end.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()