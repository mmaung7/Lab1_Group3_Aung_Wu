import guessing_game

def main():
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
