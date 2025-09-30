# Clyde Coffee Shop Simulator 4000
# Copyright(c) 2023 ClydeBank Media, All Rights Reserved.

print("Clyde Coffee Shop Simulator 4000, Version 1.00")
print("Copyright(c) 2023 ClydeBank Media, All Rights Reserved.\n")
print("Lets collect some information before we start the game.\n")

# Get name and shop name
name = input("What is your name? ")
shop_name = input("what do you want to name your coffee shop? ")
print("\nThanks, " + name + ". Let's set some initial pricing.\n")

# Get initial price of a cup of coffee
cup_price = input("what do you want to charge per cup of coffee? ")

# Display what we have 
print("\nGreat. Here's what we've collected so far.\n")
print("You're name is " + name + " and you're opening " + shop_name + "!")
print ("Your first cup of coffee will sell for $" + cup_price + ".\n")