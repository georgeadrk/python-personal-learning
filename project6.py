import random as rd

print('Welcome to Rock, Paper, or Scissors!')

win: int = 0
lose: int = 0
draw: int = 0

while True:
    choices: list = ['rock', 'paper', 'scissors']
    computer_choice = rd.choice(choices)

    player_choice: str = input('\nRock, Paper, or Scissors? ').lower()
    if player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
        print('Try again! Please input a valid move!')
        continue

    print(f'Player choice: {player_choice}')
    print(f'Computer choice: {computer_choice}')

    if (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        print('You win!')
        win += 1
    elif (computer_choice == 'rock' and player_choice == 'scissors') or (computer_choice == 'paper' and player_choice == 'rock') or (computer_choice == 'scissors' and player_choice == 'paper'):
        print('You lose!')
        lose += 1
    else:
        print('Draw!')
        draw += 1

    print('\nStats:')
    print(f'Win: {win}')
    print(f'Lose: {lose}')
    print(f'Draw: {draw}')

    option: str = input('Play again? (Y/N) ').upper()
    if option == 'Y':
        continue
    else:
        print('Thanks for playing!')
        exit()