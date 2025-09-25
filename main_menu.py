# Lab 1
# Group: 3
# Authors: Cheng Hao Wu, Myint Myat Aung
# Date: 9/24/2025

import guessing_game
import rock_paper_scissors_game

def main():
    """
    Display the main menu and let the user choose a game.

    Options:
        1. Play the Guess the Number game
        2. Play the Rock-Paper-Scissors game
        3. Exit the program

    Based on the choice, the corresponding game function is called.
    If Exit is chosen, the program prints a goodbye message and terminates.

    Author: Myint Myat Aung/Cheng Hao Wu
    """
    print("Which game do you want to play?")
    print("1. Guess the Number")
    print("2. Rock, Paper, Scissors")
    print("3. Exit")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        guessing_game.guessing_game()
    elif choice == "2":
        rock_paper_scissors_game.rock_paper_scissors()
    elif choice == "3":
        print("Goodbye!")
        exit()
        
if __name__ == "__main__":
    main()
