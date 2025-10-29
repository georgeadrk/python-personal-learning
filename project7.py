import random as rd

print('Guess The Number (1-100)')

while True:
    computer_num: int = rd.randint(1, 100)
    attempts: int = 1
    while attempts <= 7:
        guess: int = int(input('\nYour guess: '))

        if guess == computer_num:
            print(f'That\'s right! The number is {computer_num}!')
            print(f'You guessed it correctly in {attempts} attempts!')
            break
        elif guess < computer_num:
            print('Too low!')
            attempts += 1
        else:
            print('Too high!')
            attempts += 1

    if attempts == 7:
        print('\nYou ran out of attempts!')

    option: str = input('\nWould you like to play again? (Y/N) ').upper()
    if option == 'Y':
        continue
    elif option == 'N':
        print('Goodbye!')
        exit()