# logic comparisons
#If statements
a = "yes"
b = "yes"
if a == b:
    print("a is equal to b")
#
# note that assigning a value is with a single equal sign
# while checking for equality is with a double equal sign
#
a = "yes"
b = "no"
if a == b:
    print("a is equal to b")
# this will not print anything because a is not equal to b
#
a = "yes"
b = "no"
if a == b:
    print("a is equal to b")
    print("Really, it is, I promise!")
else:
    print("a is not equal to b")
# Else is the "otherwise" statement
# You can have only one else statement for each if statement
#
# Elif statements(else if)
a = 1
b = 2
c = 3 
if a > b:
    print("a is greater than b")
elif b < c:
    print("a is less than b")
# If you use a else statement, it must be the last statement after the elif statements
#
#Nested comparisons
a = 1
b = 2
c = 3

if a > b:
    print("a is greater than b")
    if b != c:
        print("but b is not equal to c")
    else:
        print("b is equal to c  ")
else:
    print("a is less than b")
#
# Loops
# For
#
# Display the planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# for each planet in the list of planets, print the planet
for planet in planets:
    print(planet)
#
# Iterate through a string
a = "Hello, World!"
for letter in a:
    print(letter)
# Modify a temporary variable
singular_words = ["student", "teacher", "room"]
for word in singular_words:
    print(word + "s")
else:
    print("done")
#
# Range function
# Used to generate a sequence of numbers
# Display the numbers first 10 numbers
for number in range(10):
    print(number)
    
#
# The planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#
# Display the planets with their number
for index, value in enumerate(planets):
    print(index + 1, value)
#    
# While loops
# while number is < 10, display number
number = 1
# create a infinite loop
# while number < 10:
#    print(number)
#    number += 1
#    while True:
#        print("It's true")

bottles = 99
while bottles > 0:
    print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer.")
    bottles -= 1
    print("Take one down and pass it around,", bottles, "bottles of beer on the wall.")
while True:
    print("Hello, World!")
    break
# break exits the loop immediately
# if number is greater than 5, exit the loop
for i in range(10):
    print(i)
    if i > 5:
        break
    
# if the number is divisible by 2, print it
for i in range(10):
    if i % 2: continue
    print(i)
    
# Nested loops
for i in range(10):
    for j in range(10):
        print(str(i) + (str(j)))