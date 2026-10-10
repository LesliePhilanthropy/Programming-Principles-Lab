#Program Name: Lab1.py
#Course: IT1114/Section 81538
#Student Name: Leslie Lawrence
#Assignment Number: Lab5
#Due Date: 10/04/2026
#Purpose: Calculate the amount and cost of purchasing flooring.
#PyCharm, YouTube

# Get the monthly sales goal
sales_goal = float(input("Sales Goal: "))

# Variables to total sales and sales goals
total_salespeople = 0
department_total_sales = 0

# Loop 1 Process each salesperson
another_salesperson = 'y'
while another_salesperson.lower() == 'y':
    total_salespeople += 1
    salesperson_total = 0

    # Loop 2 Gather 4 weeks of sales for each individual salesperson
    for week in range(1, 5):
        prompt = f"Salesperson {total_salespeople} week {week} :"
        weekly_sale = float(input(prompt))
        salesperson_total += weekly_sale

    # Add the salespersons monthly total to the entire department total
    department_total_sales += salesperson_total

    # Go back to see if there is anyone else to process
    another_salesperson = input("Another Salesperson: ")

# Calculate manager bonus based on the sales goal
if department_total_sales > sales_goal:
    bonus_rate = 0.05
else:
    bonus_rate = 0.02

manager_bonus = department_total_sales * bonus_rate

# Outputs
print(f"Number of employees: {total_salespeople}")
print(f"Department Sales Goal: {sales_goal}")
print(f"Total Sales: {department_total_sales}")
print(f"Manager Bonus: {manager_bonus}")
