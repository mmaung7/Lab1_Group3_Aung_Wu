import random
import main_menu

def rock_paper_scissors():

  while True:
    print('Welcome to Rock-Paper-Scissors!')
    print('Choose your move:')
    print('1. Paper')
    print('2. Scissors')
    print('3. Rock')

    try:
      user_choice = int(input('Enter your choice (1, 2, 3): '))
      if user_choice not in [1, 2, 3]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue
      
        
