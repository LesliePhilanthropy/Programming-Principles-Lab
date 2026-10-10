#Program Name: Lab1.py
#Course: IT1114/Section 81538
#Student Name: Leslie Lawrence
#Assignment Number: Lab1
#Due Date: 09/06/2026
#Purpose: Calculate the amount and cost of purchasing flooring.
#PyCharm, YouTube

#Inputs
length = float(input("Room Length"))
width = float(input("Room Width"))
cost = float(input("Floor Cost Per Square Foot"))

#Equation to calculate square feet
square_feet = length * width

#Multiply cost per sq ft by total sq feet
flooring = square_feet * cost

#Add in taxes
taxes = 0.07

floor_with_taxes = flooring * taxes

total = floor_with_taxes + flooring

#Put it all together

#output
print("Square feet", square_feet)
print("Flooring", flooring)
print("Tax", floor_with_taxes)
print("Total", total)