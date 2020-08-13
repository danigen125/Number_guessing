import math
from random import seed
from random import randint

seed(1)

for _ in range(100):
    value = randint(0, 100)

type(int(value))

x = input('Write any number between 0 and 100: ')
type(int(x))

def ifLower():
    global z
    type(int(z))
    z = value - x
    x + z
    print("You didn't get the correct answer!")
    print("I needed to add " + z + " to your number!")
    print('The number was  ' + value + ' !')
    print("You Really don't get it")

def ifEquals():
    print("You got the correct number!")
    print("   How lucky for you!")

def ifGreater():
    global z
    type(int(z))
    z = value - x
    abs(z)
    print("You didn't get the correct answer, don't even think about it!")
    print("I needed to lower the number with " + z + " !")
    print("The number was " + value + "!!!!")
    print("STUPIDITY IS NOT RIGHT!")

if x > value:
    ifGreater()

if x < value:
    ifLower()

if x == value:
    ifEquals()