import random

num_to_guess = random.randint(1, 100)

user_num = 0
while user_num != num_to_guess:
    try:
        user_num = int(input("Guess the number: "))  # to handle Value error if user input isn't number
    except ValueError:
        print("It's not a number!")
        continue
    if user_num < num_to_guess:
        print("To small!")
        continue
    elif user_num > num_to_guess:
        print("To big!")
        continue
print("You win!")
