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

    comp_choice = random.randint(1, 3)
    choices = {1: 'Paper', 2: 'Scissors', 3: 'Rock'}
    print(f'You chose: {choices[user_choice]}')
    print(f'Computer chose: {choices[comp_choice]}')

    if user_choice == comp_choice:
      print('It's draw')
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
      print('You win!')
    else:
      print('You lose!')
      
      
        
