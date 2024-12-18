# compucter guesses a number between 1 and 100
# user tries tu guess this number
# if gusess is lower than the number:
# the program informs guess higher
# else if the number is higher, then:
# the program informs guess lower
#

import random

number_target = random.randint(1, 100)

number_of_guesses = 0
number_lower = 1
number_upper = 100

while True:
    # number_guess = int(input("Uzmini skaitli starp 1 un 100: "))
    number_guess = random.randint(number_lower, number_upper)

    number_of_guesses += 1

    if number_guess == number_target:
        if number_of_guesses <= 3:
            print(f"Wow, you are a super player, you won from {number_guess} guesses!")
        elif number_of_guesses <= 10:
            print(f"Nice, you have won after {number_of_guesses} guesses!")
        else:
            print(f"Well, you could have done better than {number_of_guesses} guesses...")
        break
    elif number_guess < number_target:
        print("Guess higher")
        number_lower = number_guess + 1
    elif number_guess > number_target:
        print("Guess lower")
        number_upper = number_guess - 1

   
    if number_of_guesses > 5 and number_of_guesses <= 10:
        print("Still guessing? You've got this... maybe.")
    elif number_of_guesses > 10 and number_of_guesses <= 15:
        print("You sure you're not just playing with me?")
    elif number_of_guesses > 15 and number_of_guesses <= 20:
        print("Wow, the number must be running circles around you by now!")
    elif number_of_guesses > 20:
        print("Okay, this is getting serious. Maybe the number's taking a vacation.")