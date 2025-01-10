from datetime import datetime

age = int(input("What is your age? "))
retirement_year = int(input("At what age would you like to retire? "))
years_left = retirement_year - age
current_year = datetime.now().year

print()
print(f"It's {current_year}. You will retire in {current_year + years_left}.")
print(f"You have only {years_left} years of work to go!")
