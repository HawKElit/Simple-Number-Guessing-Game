import random
random_number = random.randint(1, 100)
while True:
    user_guess = int(input("Guess a number thats between 1 and 100:"))
    if user_guess > random_number:
        print('Your guess is too high, try again!')
    elif user_guess < random_number:
        print('Your guess is too low, try again!')
    if user_guess == random_number:
        print('You got it right!')
        break
