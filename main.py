import random

# Rock = R, Paper = P, Scissors = S
possible_options = ['R', 'P', 'S', ]

while True:
    users_input = str(input('Pick an option between R, P and S: '))
    users_choice = users_input.upper()
    computer_choice = random.choice(possible_options)


    for option in possible_options:
    
    
        while users_choice not in possible_options:
            users_input = str(input('Invalid option, please choose between R, P and S: '))
            users_choice = users_input.upper()

    print(f'Player ({users_choice}) : CPU ({computer_choice})')        

    if computer_choice == users_choice:
        print('this is a tie')
        continue

    elif users_choice == 'R':
        if computer_choice == 'S':
            print("Player wins!")
        else:
            print('CPU wins!')
            break

    elif users_choice == 'P':
        if computer_choice == 'R':
            print('Player wins!')
        else:
            print('CPU wins!')
            break

    elif users_choice == 'S':
        if computer_choice == 'P':
            print('Player wins!')
        else:
            print('CPU wins!')
            break

    else:
        break
           

        



        
       