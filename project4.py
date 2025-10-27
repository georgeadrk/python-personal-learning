import random as rd

secret: int = rd.randint(1, 100)
attempts: int = 0

print('I\'m thinking of a number between 1 and 100')

while True:
    guess: int = int(input('Your guess: '))
    attempts += 1

    if guess < secret: print('Too low!')
    elif guess > secret: print('Too high!')
    else:
        print(f'Correct! You guessed it in {attempts} tries.')
        break