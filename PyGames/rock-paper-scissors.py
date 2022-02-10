import random

user_wins = 0
bot_wins = 0
print("-------------------------------------------------------")
print("Welcome to my Rock Paper and Scissors Game!!!")

options = ["rock", "paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q".lower():
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!!!")
        user_wins += 1
        continue

    elif user_input == "sissors" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!")
        user_wins += 1
        continue

    else:
        print("You lost!!")
        bot_wins += 1 

print("-------------------------------------------------------")
print("You won", user_wins, "times.")
print("The computer won", bot_wins, " times.")
print("Thanks for playing!!! Goodbye!!")
