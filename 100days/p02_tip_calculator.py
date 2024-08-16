print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? %"))
number_of_people = int(input("How many people to split the bill? "))
bill_per_person = float(total_bill + total_bill * tip_percentage / 100) / number_of_people
result = round(bill_per_person, 2)
result = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${result}")