# Clyde Coffee Shop Simulator 4000
# Copyright(c) 2023 ClydeBank Media, All Rights Reserved.

# import items from the random module to generate weather
from random import seed
from random import randint
#current day number 
day = 1

#starting cash on hand
cash = 100.00

#coffee on hand (cups)
coffee = 100

# Sales list of dictionaries
sales = [
    {
        "day": 1,
        "coffee_inv": 100,
        "advertising": "10",
        "temp": 68,
        "cups_sold": 16,
    },
    {
        "day": 2,
        "coffee_inv": 84,
        "advertising": "15",
        "temp": 72,
        "cups_sold": 20,
    },
    {
        "day": 3,
        "coffee_inv": 64,
        "advertising": "5",
        "temp": 78,
        "cups_sold": 10,
    },
    ]

# create an empty sales list
sales= []

# print welcome message
print("Clyde Coffee Shop Simulator 4000, Version 1.00")
print("Copyright(c) 2023 ClydeBank Media, All Rights Reserved.\n")
print("Lets collect some information before we start the game.\n")
#
# Get name and shop name using the following approach:
# set name and shop_name to False  
# use while not name and not shop_name to continue to prompt for a non-empty string


name = False
while not name:
    name = input("what is your name? ")
    
shop_name = False
while not shop_name:
    shop_name = input("what do you want to name your coffee shop? ")

# we have what we need , so let's get started!

print("\nOk, let's get started. Have fun!")

# the main game loop
running = True
while running:
    # display the day and add a "fancy" text effect
    print("\n-----/Day " +str(day) + " @ " + shop_name + " |-----")
    
    # generate a random temperature between 20 and 90 
    # we'll consider seasons later on, but this is good enough for now
    temperature = randint(20, 90)
    # display the cash and weather
    print("you have $" +str(cash) + " cash on hand and the temperature is " + str(temperature) + ".")
    print("You have enough coffee on hand to make " + str(coffee) + " cups.\n")
    
    # get price of cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")
    
    # get price of cup of coffee
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much do you want to spend on advertising (0 for none)? ")
    
    # convert advertising into a float
    # if it fails, assign it to zero
    try:
        advertising = float(advertising)
    except ValueError:
        advertising = 0
        
    # deduct advertising from cash on hand
    cash -= advertising 
    
    # TODO: Calculate today's performance
    # TODO: Display today's performance
    
    #before we loop around, add a day
    day += 1
    