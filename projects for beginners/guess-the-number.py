import random

print('Number Guessing Game')

number =random.randint(1,15)

chances=0

while chances < 5:
    guess=int(input('Enter a number between(1-15):'))
    
    if guess == number:
        print('CONGRATULATION YOU WON!')
        break
    elif guess < number:
        print('Your guess is too low')
    else:
        print('Your guess is too high')


    chances += 1

if not chances > 5:
        print('You loose the number was' , number)