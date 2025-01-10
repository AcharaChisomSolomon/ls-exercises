def display_formatter(string):
    return f"==> {string}"

print(display_formatter("Enter the first number:"))
num1 = float(input().strip())
print(display_formatter("Enter the second number:"))
num2 = float(input().strip())

print(display_formatter(f"{num1} + {num2} = {num1 + num2}"))
print(display_formatter(f"{num1} - {num2} = {num1 - num2}"))
print(display_formatter(f"{num1} * {num2} = {num1 * num2}"))
print(display_formatter(f"{num1} / {num2} = {num1 / num2}"))
print(display_formatter(f"{num1} // {num2} = {num1 // num2}"))
print(display_formatter(f"{num1} % {num2} = {num1 % num2}"))
print(display_formatter(f"{num1} ** {num2} = {num1 ** num2}"))
