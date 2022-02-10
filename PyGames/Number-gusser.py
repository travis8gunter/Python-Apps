import random

#-------------------------------------------INTO--------------------------------------
print("---------------------------------------------------------------------------")
print("Welcome to my Number Guessing Game!!")
print("First type a number that sets the Max # of what you want to be guessing!")
print("---------------------------------------------------------------------------")
#-------------------------------------------GAMESTART-----------------------------------


top_of_range = input("Type any number: ")
print("Guess a number between 1 -",top_of_range)


#----------------------------------------Checks-if-digit-----------------------------------
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number that is larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
print("---------------------------------------------------------------------------")

#----------------------------------------While-Loop-tries-----------------------------------
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    print("---------------------------------------------------------------------------")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
#-------------------------------------------End-Closing-----------------------------------
    if user_guess == random_number:
        print("You guessed the number!!")
        print("You WIN!!! Run to Play again!")
        break
    else:
        if user_guess > random_number:
            print("Your guess is to high!")
        else:
            print("Your guess was to low")
print("You guessed the correct number in", guesses, "tries!!")
print("---------------------------------------------------------------------------")

