import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'programs')) # directory thing (i do not understand)

def main():
    while True:
        print("\nChoose an option:")
        print("[1] Number System Converter\n[2] Random Character Guesser\n[end] End the program")
        
        choice = input("Enter your choice. Press 'end' to exit: ").strip()

        if choice == "1":
            import Number_System_Converter
            Number_System_Converter.main()
        elif choice == "2":
            import Random_Character_Guesser
            Random_Character_Guesser.main()
        elif choice.lower() == "end":
            print("Session end.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
