
print("------------------------------------------------------------------------------")
print("HELLO AND WELCOME TO THIS FORREST ESCAPE GAME!!!!")
print("TRY TO FIND YOUR WAY OUT OF THE FORREST AND WATCH OUT FOR DANGERS")
print("------------------------------------------------------------------------------")
name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")
print("You are in a Dark Forrest, you need to find a way out to somewhere safe.")
print("------------------------------------------------------------------------------")
answer = input("The road has three ways to go... UP, RIGHT, LEFT:  ").lower()

if answer == "left":
    print("------------------------------------------------------------------------------")
    print("You went left into a new road.")
    answer = input("You find a Castle and Knight Troops....CASTLE, or TROOPS: ").lower()
    if answer == "castle":
        print("------------------------------------------------------------------------------")
        print("You went inside and the KING gives you everything you need! YOU WIN!!!!")
    elif answer == "troops":
        print("------------------------------------------------------------------------------")
        print("The Knight TROOPS mistake you as a bandit and slay you... YOU LOSE!!!")

elif answer == "right":
    print("------------------------------------------------------------------------------")
    print("You went to the Right down the road.")
    answer = input("The road comes to Cave.... ENTER, or BACK: ").lower()
    if answer == "enter":
        print("------------------------------------------------------------------------------")
        print("You walk into the Cave and you see a BEAR charging you!! You LOSE")
    elif answer == "back":
        print("------------------------------------------------------------------------------")
        print("You turned around and went back.")


elif answer == "up":
    print("------------------------------------------------------------------------------")
    print("You went UP and find a bridge, you need to get to the other side.")
    answer = input("how should you pass.... CROSS or SWIM: ").lower()
    if answer == "cross":
        print("------------------------------------------------------------------------------")
        print("You CROSSED the bridge!")
        answer = input("After the bridge you see a Castle and a small Hut ahead....CASTLE, or HUT: ").lower()
        if answer == "castle":
            print("------------------------------------------------------------------------------")
            print("You went inside and the KING gives you everything you need! YOU WIN!!!!")
        elif answer == "hut":
            print("------------------------------------------------------------------------------")
            print("You enter the HUT and a hungry WITCH is inside waiting... YOU LOSE!!!")
            
    elif answer =="swim":
        print("------------------------------------------------------------------------------")
        print("You SWIM and get eaten by a shark!! YOU LOSE!!")

    

else:
    print("------------------------------------------------------------------------------")
    print("Not a valid input, you LOSE. Type what options the prompt gives you.")