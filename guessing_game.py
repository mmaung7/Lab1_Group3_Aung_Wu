import random
import main_menu

def guessing_game():
    target = random.randint(1, 100)
    print(target)
    play = True
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Guess what it is. You have 5 tries: ")
    guess = input()
    for i in range(4, 0, -1):
        if int(guess) < target:
            print("Your guess is too low. You have", i, "tries left.")
            guess = input()
        elif int(guess) > target:
            print("Your guess is too high. You have", i, "tries left.")
            guess = input()
        else:
           print("Congratulations! You've guessed the number!")
           break
        if i == 1 and int(guess) != target:
            print("Sorry, you've used all your tries. The number was", target)
    print("Do you want to play again? (yes/no)")
    again = input().lower()
    if again == "no":
        main_menu.main()
    elif again == "yes":
        guessing_game()
            

#guessing_game()
    
    