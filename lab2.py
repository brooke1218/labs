"""
homework1
Maggie O'Brien
"""


print('Hello! This program calculates mpg.')

def miles_per_gallon(mpg):
    """
    Calculates miles per gallons
    miles: positive float
    gallons: positive float
    """

    miles = input('Enter the miles traveled: ')
    miles = float(miles)
    gallons = input('Enter gallons used: ')
    gallons = float(gallons)

    mpg = miles / gallons
    return mpg

mpgResult = str(miles_per_gallon(mpg))
print("Your miles per gallon is " + mpgResult)


def ten_random_numbers(start = float, stop = float):
    import random
    """
    Prints ten random integers between start and stop
    """

    print('Hello! This program generates 10 random integers between two numbers.')
    start = input('Enter the first number: ')
    start = float(start)
    stop = input('Enter the second number: ')
    stop = float(stop)

    for i in range(10):
        n = random.randint(start,stop)
        print("Random Number: ", n)

def circle_area():
    """
    Calculates the area of a circle given the radius.
    radius: non-negative float
    returns: float
    """

    print("Hello! this calculates the area of a circle")
    from math import pi
    radius = float(input("Enter the radius of the circle: "))
print("The area of the circle with radius of " + str(radius) + " is " + str(pi * radius**2))
