name = input('Type your name: ').title()
print(f'Welcome {name} to the adventure...')

answer = input('You are on a dirt road, it has come to an end... Type left or right: ').lower()

if answer == 'left':
    answer = input('You have come to a river, swim across or walk around. Type walk or swim: ').lower()

    if answer == 'swim':
        print('You swam across and eaten by croc!')
    elif answer == 'walk':
        print('You walked for many kilometers and starved...')
    else: 
        print('Not a valid option...')
elif answer == 'right':
    answer = input('You chose to go right and found a treasure chest! Would you like to take the treasure.. Type yes or no: ').lower()

    if answer == 'yes':
        print('The treasure was too heavy and you became dehydrated and eaten by lions..')
    elif answer == 'no':
        print('A man sees you leaving the treasure and helps you carry it with his horse... You WIN... You\'re rich!!')
    else:
        print('Not a valid option...')

else:
    print('Not a valid option...')
