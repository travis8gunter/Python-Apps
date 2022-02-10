print("Welcome to my Game of Thrones game!!")
playing = input("Do you want to play? Insert 'Yes' or 'quit' to exit:  ")


if playing.lower() != "yes":   
    quit()
print("Okay lets play!!")
print("--------------------------------------------------------------------------------")
print("These questions will be from the Show, warning SPOLIERS!!")
score = 0
print("--------------------------------------------------------------------------------")

#-----------------Question1--------------------------
anwser = input("How many Dragons does Daenerys Targaryen have?: ")
if anwser.lower() == "3":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("--------------------------------------------------------------------------------")

#------------------Question2----------------------
anwser = input("What is the name of the Fort that Jon Snow guards at the Wall?: ")
if anwser.lower() == "castle black":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("--------------------------------------------------------------------------------")

#------------------Question3----------------------
anwser = input("What is the name of the Leader of the White Walkers?: ")
if anwser.lower() == "night king":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("--------------------------------------------------------------------------------")

#------------------Question4----------------------
anwser = input("What is the name of Jon Snow's direwolf?: ")
if anwser.lower() == "ghost":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("--------------------------------------------------------------------------------")

#------------------Question5----------------------
anwser = input("What is the name of the main Castle in the North?: ")
if anwser.lower() == "winterfell":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " out of 5!!")
print("You got " + str((score / 5) *100) + "%.")
