# Program Name: Lab4.py
# Course: IT1114/Section 81538
# Student Name: Leslie Lawrence
# Assignment Number: Lab2
# Due Date: 09/27/2026
# Purpose: Calculate bank balances and interest
#PyCharm, Usando Python on YouTube


# What the program should accept
balance = float(input("Beginning Balance "))
interest_rate = float(input("Monthly Interest Rate "))
months = int(input("Number of months "))

# How to convert percentage to decimal
interest_rate = interest_rate / 100

# Heading for the table that the print function will display
print("\nMo.No. Interest Balance")

# Calculate interest and balance for each month
for month in range(1, months + 1):
    interest = balance * interest_rate
    balance = balance + interest

    print(month, interest, balance)