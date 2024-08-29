# SpencerP1.py
# Programmer: Andrew Spencer (aspencer22@cnm.edu)
# Date: 08/28/2024
# Purpose: Provides a user the capability to calculate the surface area and the volume of a square pyramid.
# Python Version: 3.12.5
from math import sqrt
import time

# Display a header explaining the program
print('\nWelcome to Pyramid Palooza!')
print('Get ready for a fun-filled calculation session.\nProvide your pyramid’s base length and height, \nand the volume and surface area will be revealed with pizzazz!')
print('To get started, please follow through the prompts and provide the necessary values.\n')
# Have user provide the length of the base for the pyramid
base_length = float(input('Please enter the length of the base of the pyramid: '))

# Have user provide the height of the pyramid
height = float(input('Please enter the height of the pyramid: '))
print('Calculating the volume and surface area of your pyramid...')
time.sleep(2)
print('\n\n')

# Calculate the volume of the pyramid
volume = base_length ** 2 * height / 3

# Interim interactive message
print('Calculations complete!\n')
time.sleep(1)
print('A pyramid with a base length of', base_length, 'and a height of', height, 'has the following properties:')

# Display the volume of the pyramid
print('The Volume of your pyramid is:', volume)

# Calculate the slant height of the pyramid using Pythagorean Theorem
slant_height = sqrt((base_length / 2) ** 2 + height ** 2)

# Display slant_height result
print('The Slant Height of your pyramid is:', slant_height)

# Calculate the surface area of the pyramid
surface_area = 2 * base_length * slant_height

# Display the surface area of the pyramid
print('The Surface Area of the pyramid is:', surface_area)

# Thank the user for using the square pyramid calculator
time.sleep(4)
print('\n\nThank you for using Pyramid Palooza!\nI hope you enjoyed using this awesome program!')
print('For more awesome programs, check my github out at:')
print('')
