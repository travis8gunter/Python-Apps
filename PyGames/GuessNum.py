import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number!: "))
    if user == number:
        print("Good Job you got it!!")
        print(f"You guessed the number right it is {number}")
        break
if user != number:
    print(f"Your guess was not correct the number is{number}")