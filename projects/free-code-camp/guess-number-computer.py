import random
def guess(number):
    random_number = random.randint(1, number)
    guess_number = 0
    while(guess_number != random_number):
        guess_number = int(input(f"Enter a number (1 - {number}): "))
        if guess_number < random_number:
            print("Too low!")
        elif guess_number > random_number:
            print("Too high!")
    print("Congrats! You finish the game!")
guess(100)