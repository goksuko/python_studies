from math import exp, log
import time
import numpy as np

portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = int(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
monthly_salary = annual_salary / 12

def savings_in_36(portion_saved, monthly_saved, semi_annual_raise, current_savings):
    inc  = 0
    for n in range(36):
        current_savings = (current_savings + monthly_saved) * (1 + r / 12)
        inc += 1
        if inc == 6:
            monthly_saved *= 1 + semi_annual_raise
            inc = 0
    return current_savings

step = 0
min = 0
max = 10000
guess = (min + max) / 2

res = 0
while (abs(res - total_cost * portion_down_payment) > 100):
    res = savings_in_36(guess / 10000, monthly_salary * guess / 10000, semi_annual_raise, current_savings)
    if res > total_cost * portion_down_payment:
        max = guess
    else:
        min = guess
    guess = (min + max) / 2
    step += 1
    if step > 14:
        break

portion_saved = guess / 10000

if step > 14:
    print("It is not possible to pay the down payment in three years.")
else: 
    print(f"Best savings rate: {portion_saved}")
    print(f"Steps in bisection search: {step}")
                          