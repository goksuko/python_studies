from math import exp, log

portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

month = 0
while(current_savings < total_cost * portion_down_payment):
    current_savings = (current_savings + monthly_saved) * (1 + r / 12)
    month += 1

print(f"Number of months: {month}")
                          