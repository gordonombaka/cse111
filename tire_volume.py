"""
Author: Gordon Ombaka
Date: 22nd Sep 2024
Purpose: Python program that gets input from a user, performs arithmetic, 
         and displays results for the user to see.

"""

import math
from datetime import datetime

# Print a description for the user to see about the program

print("This program computes and outputs the volume of space inside a tire.")
print()

# Get inputs from the user

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

print()

# Computate the volume of the tire

numerator_outbracket = math.pi * width**2 * aspect_ratio
numerator_inbracket = width * aspect_ratio + (2540 * diameter)
numerator = numerator_outbracket * numerator_inbracket
volume = numerator / 10000000000

# Round off volume to 2 d.p

volume = round(volume, 2)

# print output for the user to see

print(f"The approximate volume is {volume} liters")

"""
After your program prints the tire volume to the terminal window, 
your program should ask the user if she wants to buy tires with the dimensions that she entered. 
If the user answers “yes”, your program should ask for her phone number and store her phone number in the volumes.txt file.
"""

print()
print("==============================================================")

# User input

user_decision = input("Do you want to buy the tires with the dimensions you entered (Yes/No)? ")

# Computation

if user_decision.lower() == "yes":
    phone_number = input("Please provide your phone number: ")

else:

    print("Thank you. Try Checking other dimensions")

# Current date and time

current_date_and_time = datetime.now().strftime("%d/%m/%Y")

# Opens volumes.txt for appending and writing

with open("volumes.txt", "a") as volume_file:
    volume_file.write(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {volume}, {phone_number}\n")


