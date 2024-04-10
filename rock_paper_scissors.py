import random

user_wins = 0
computer_wins = 0
draw = 0

options = ['rock', 'paper', 'scissors']

while True: 
    user_input = input('Type Rock / Paper / Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue
    
    random_numer = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_choice = options[random_numer]
    print(f'Computer chose {computer_choice}.')

    if user_input == 'rock' and computer_choice == 'scissors':
        print('You won!')
        user_wins += 1
        
    elif user_input == 'paper' and computer_choice == 'rock':
        print('You won!')
        user_wins += 1
        
    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You won!')
        user_wins += 1

    elif user_input == computer_choice:
        print('A draw')
        draw += 1

    else:
        print('You lost')
        computer_wins += 1

print(f'You won {user_wins} times...')
print(f'Computer won {computer_wins} times...')
print('Goodbye')
        



