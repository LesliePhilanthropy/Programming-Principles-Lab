# Program Name: Lab2.py
# Course: IT1114/Section 81538
# Student Name: Leslie Lawrence
# Assignment Number: Lab2
# Due Date: 09/13/2026
# Purpose: Calculate parking amounts due at the KSU visitor parking lot.
# PyCharm, YouTube

# Step 1, define minutes
def calculate_parking_fee(minutes):

    # Step 2 - If, Elif, and Else Statements
    if minutes < 30:
        rate = 0.00
    elif minutes <= 60:
        rate = 1.00
    elif minutes <= 180:
        rate = 1.25
    # I got 180 by multiplying 3 hours by 60 minutes
    elif minutes <= 300:
        rate = 1.50
    else:
        rate = 2.00

    # Step 3 - Calculate the total
    parking_total = rate * (minutes / 60)

    return parking_total


# Step 4 - Get input from the user
minutes = float(input("Number of minutes parked: "))

# Step 5 - Calculate and display the total
parking_total = calculate_parking_fee(minutes)

print("Total cost:", parking_total)