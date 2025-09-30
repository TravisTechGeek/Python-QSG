# example of a list in Python
grocery_list = ["eggs", "milk", "cheese", "pasta"]
#
# items in a list are enclosed in square brackets and separated by commas
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# numbers aren't set in quotes, unless you want them to be strings
odd_numbers = [1, 3, 5, 7, 9]
# you could use a string to reference a list of items, but it would be less efficient
# and harder to manipulate than a list
grocery_list_string = "eggs, milk, cheese, pasta"
# using a list allows you to easily add, remove, or change items
# accessing items in a list is done using indexing, starting at 0
grocery_list = ["eggs", "milk", "cheese", "pasta"]
print("The first item on the list is " + grocery_list[0])
print("The second item on the list is " + grocery_list[1])
#
# lists cab have different data types, like strings and numbers
random_assortment = ["egg", "tree", 3, "green", 94, "pluto", 3.14]
# tuples are similar to lists, but they are immutable (cannot be changed)
# tuples are defined using parentheses instead of square brackets
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
# you can access items in a tuple using indexing, just like a list
# the following line will print "Mars"
print(planets[3])
# 
# sets are unordered collections of unique items
# sets are defined using curly braces or the set() function
customers = {"James Smith", "Andrea Richards", "Sam Sharp", "Brenda Longmire", "Veronica March", "Sylvia Smith", "James Smith", "Vanessa Bush", "Steve Hammersmith", "Walt Hawkins" }
#prints the set of customers
print(customers)
# 
# the following line will print the number of unique customers
customers = {
    "James Smith", 
    "Andrea Richards", 
    "Sam Sharp", 
    "Brenda Longmire", 
    "Veronica March",
    "Sylvia Smith", 
    "James Smith", 
    "Vanessa Bush", 
    "Steve Hammersmith"
}
# dictionaries are collections of key-value pairs
# dictionaries are defined using curly braces, with keys and values separated by colons
customer1 = {
    "name": "James Smith",
    "age": 24,
    "phone": "555-555-1941",
    "email": "james@xyzinternet.net"
}
customer2 = {
    "name": "Andrea Richards",
    "age": 33,
    "phone": "555-555-4928",
    "email": "andrea@coffeeloversunite.us"
}
# each key in a dictionary follows Key-Value pair
print(customer1["name"])  # prints "James Smith"

# you cannot have duplicate keys in a dictionary, if you assign a value to an existing key
# it will overwrite the previous value, as shown below
customer3 = {
    "name": "Robert",
    "name": "John" }
print(customer3)
#
# boolean Variables
# boolean variables can only have two values: True or False
# true is represented by 1 and false is represented by 0
walking = False
running = True
#
# multidemensional Lists
# daily high and low temperature (in Fahrenheit)
temps = [
    [66, 34],
    [57,25], 
    [49, 45]
]
# day 1 temps
print(temps[0])

# day 2 temps
print(temps[1])

# day 3 temps
print(temps[2])

# day 1 high
print(temps[0][0])

# day 1 low
print(temps[0][1])

# weekly (then daily) high and low temperature (in Fahrenheit)
temps = [
    [66, 34],  # day 1
    [57, 25],  # day 2
    [49, 45],  # day 3
    [45, 19],  # day 4
    [33, 7],  # day 5
    [32, 14],  # day 6
    [49, 37]   # day 7
],
[
    [52, 39],  # day 1
    [61, 51],  # day 2
    [64, 51],  # day 3
    [67, 57],  # day 4
    [69, 42],  # day 5
    [32, 14],  # day 6
    [49, 37]   # day 7
]
print(temps[1][2][1])  # prints the low temp for day 3 of week 1