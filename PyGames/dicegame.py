import random
player1 = 0
player2 = 0

die = [1,2,3,4,5,6]
def dices():
    die_num = random.choice(die)
    return die

#---------------------------Intro--------------------------
print("----------------------------------------------------------")
print("Welcome to this Pig Dice game!!")
print("Roll your dice to get points, and 'End' turn to count those points")
print("The first player to get 100 points WINS the game!!")
print("You may role your dice as many times as you want")
print("If you roll a 1 your turn is over and you dont get any points for the turn")

print("Player 1 has ", player1, " points")
print("Player 2 has ", player2, " points")
print("-----------------------------------------------------------")

#-------------------------Game----Start------------------------------

start = input("Player 1 type 'Start' to begin! ").lower()
if input == "start":
    
    

turn_one = input("Would you like to Roll or End turn? ").lower()
if input == "roll":
    
    if die_num == 1:
        
    print("You rolled a",die, "do you want to roll or try again?")
elif input =="end":
    
else:
    print("You did not enter the correct input, try again")
    
    