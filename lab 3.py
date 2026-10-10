# Program Name: Lab3.py
# Course: IT1114/Section 81538
# Student Name: Leslie Lawrence
# Assignment Number: Lab2
# Due Date: 09/20/2026
# Program Name: Lab3.py
# Purpose: Calculate food costs for the KSU CCSE Hackathon
#PyCharm, YouTube

# Variables
pizza_slices = int(input("Number of pizza slices "))
salads = int(input("Number of salads ordered "))

# Calculate whole pizzas needed when one pizza equals 12 slices
whole_pizzas = (pizza_slices + 11) // 12

# Calculate pizza and salad costs when each pizza cost 15.99 and each salad costs 7.99
pizza_cost = whole_pizzas * 15.99
salad_cost = salads * 7.99

# Calculate discounts with if statements
pizza_discount = 0
salad_discount = 0

if whole_pizzas > 10:
    pizza_discount = pizza_cost * 0.15

if salads > 10:
    salad_discount = salad_cost * 0.15

discount = pizza_discount + salad_discount

# Calculate delivery charge with if statements
delivery = (pizza_cost + salad_cost) * 0.07

if delivery < 20:
    delivery = 20

# Algorithm to find the total
total = (pizza_cost + salad_cost + delivery) - discount

# Print Statements
print("Whole Pizzas:", whole_pizzas)
print("Pizza cost:", pizza_cost)
print("Salad cost:", salad_cost)
print("Discount:", discount)
print("Delivery:", delivery)
print("Total:", total)

