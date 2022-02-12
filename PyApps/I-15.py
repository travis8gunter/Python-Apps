print("""Welcome to the highway travel advisor.
This app is made to work with travel on I-15 in Utah.
We will ask some questions than give you travel advice!""")

mile = input("What I-15 Mile Marker will you Enter on? ")
end = input("What I-15 Mile Marker will you Exit on? ")
time = input("How many hours from now do you want to arrive? ")
speed = input("What will be the average MPH you go? ")

speed = int(speed)
mile = int(mile)
time =  int(time)
end = int(end)


newMile = end - mile
newTime = speed * newMile


print("You will travel,",newMile,"miles")


if newMile * newTime <= 120:
    print("That is dangerosuly high. Slow down.")
    print("Thank you for using this travel advisor!") 
elif newMile/newTime >= 65:
    print("That is to slow, speed up!")
    print("Thank you for using this travel advisor!")
else:
    print("Thanks for using our service!!")




