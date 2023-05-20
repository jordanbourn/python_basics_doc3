#Module should have the following capabilities:
#1) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area
#2) Has a function to calculate the circumference of a circle
#Program in Jupyter Notebook should take in user input and use imported functions
#to calculate a circle's circumference or a houses square footage

import math

area_length = ()
area_width = ()

def area_of_a_house(area_length, area_width):
    """Calculate the square footage of a house."""
    square_footage = area_length * area_width
    print(square_footage)


circle_radius = ()

def circumference_of_a_circle(circle_radius):
    """Calculate the circumference of a circle."""
    circle_circumference = 2 * math.pi * circle_radius
    print(circle_circumference)


math_functions = True
while math_functions == True:
    user_input = input('Calculate the square footage of a HOUSE or circumference of a CIRCLE? Enter QUIT to exit.\n')
    if user_input == 'HOUSE':
        length_input = input('Enter the length of your house.\n')
        width_input = input('Enter the width of your house.\n')
        area_of_a_house(int(length_input), int(width_input))
    if user_input == 'CIRCLE':
        circle_input = input('Enter the radius of your circle.\n')
        circumference_of_a_circle(int(circle_input))
    if user_input == 'QUIT':
        math_functions = False