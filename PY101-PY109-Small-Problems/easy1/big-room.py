def console_display_formatter(string):
    return f"==> {string}"

print(console_display_formatter("Enter the dimensions of the room in m(meters) below:"))

length = float(input(console_display_formatter("Length: ")))
width = float(input(console_display_formatter("Width: ")))

print()
area = length * width
area_in_feet = area * 10.7639

print(console_display_formatter(f"Area is {area} square meter(s)"))
print(console_display_formatter(f"Area is also {area_in_feet} square feet(s)"))