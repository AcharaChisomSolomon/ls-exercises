def console_display_formatter(string):
    return f"==> {string}"

bill = float(input(console_display_formatter("What is the bill? ")))
percentage = float(input(console_display_formatter("What is the tip percentage? ")))
print()

tip = (percentage / 100) * bill
total_bill = tip + bill
print(console_display_formatter(f"The tip is ${tip:.2f}"))
print(console_display_formatter(f"The total is ${total_bill:.2f}"))