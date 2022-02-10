# instructions
print("""Welcome to the rainwater tank calculator.
We'll ask you for a few parameters about your
rainfall and rain catchment area.  Then, we'll
tell you how big to make your tank.  We assume
that your catchment area is rectangular.""")

# get width, height
inches = input("How many inches of rain fall in a large storm?-->")

width=input("How wide is your catchment area, in feet?-->")

length=input("How long is your catchment area, in feet?-->")
#get area and turn into int numbers

area = int(width) * int(length) 
#harvested water= Catchment area * rainfall * conversion factor .623
harv = int(area) * int(inches) * .623
print("You need a tank with", harv, "gallons capacity")
#Print result
print("WE HOPE YOU ENJOYED,RUN TO PLAY AGAIN")


#find volume
#feet = inches /12
#volume = length * width * height
#gals = cubicFeet *7.48




