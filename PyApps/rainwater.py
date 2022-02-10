print("""Welcome to the rainwater tank calculator!!
We will ask some questions about your rainfall catchment area!
Then we will tell you how big to make your take!""")
inches = input("How many inches of rain fall in a large storm? ")
width = input("How wide is your catchment area, in feet?")
length = input("How long is your catchment area, in feet?")
#This was just the intro of questions and getting the user data

length = int(length)
width = int(width)
inches = int(inches)
#Turned all the string inputs into ints so they could calculate
#Got the area from the userdata
area = int(length * width)
#Calculated the gallons they would need.
total = inches * area * .623
#OutPut is the printing statmetn of changing the data to float and giving the number to the user
print("You will need ",float(total), "gallon capacity to catch the most rain at one time")
