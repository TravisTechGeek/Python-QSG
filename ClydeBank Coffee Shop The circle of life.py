# ClydeBank Coffee Shop Simulator 4000
# Copyright 2002 (c) ClydeBank Media, All Rights Reserved
#
# import items from the random module to generate weather
from random import seed
from random import randint

# current day number
day = 1

# Starting cash on hand
cash = 100.00

# Coffee on hand (cup)
coffee = 100

#sales list of dictionaries
sales = [
    {
        "day": 1,
        "coffee_inv": 100,
        "advertising": 10,
        "temp": 68,
        "cups_sold": 16
    },
    {
        "day": 2,
        "coffee_inv": 84,
        "advertising": 15,
        "temp": 72,
        "cups_sold": 20
    },
    {
        "day": 3,
        "coffee_inv": 64,
        "advertising": 5,
        "temp": 78,
        "cups_sold": 10
    }
]
# create a empty sales list
sales = []

#print welcome message
print("Welcome to the ClydeBank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright 2002 (c) ClydeBank Media, All Rights Reserved.\n")

# Get name and shop name
name = input ("What is your name? ")
shop_name = input ("What do you want to name your coffee shop? ")

print("\n Ok, Let's get started. Have fun!")

#the main game loop
running = True
while running:
#   Display the day and add a "fancy" text effect
    print("\n_ _ _ _ _| Day " + str(day) + "@" + shop_name + " | _ _ _ _ _")
    
# Generate a temperature between 20 and 90 degrees
# We'll consider seasons later on, but this is good for now
temperature = randint(20,90)
# display the cash and weather
print("you have $" + str(cash) + " cash and its" + str(temperature) +"degrees.")
print("you have " + str(coffee) + " cups of coffee on hand.")

# get price of a cup of coffee
price = float(input("What do you want to charge for a cup of coffee? $")) 
print("\n You can buy advertising to help promote sales.")
advertising = float(input("How much do you want to spend on advertising? $"))
#deduct advertising from cash
cash -= advertising
#todo calculate todays performance
#display todays performance

#before we loop back to the start, increment the day
day += 1    