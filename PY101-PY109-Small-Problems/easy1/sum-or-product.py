number = int(input("Please enter an integer greater than 0: "))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')
print()

if operation == "s":
    sum = 0
    for i in range(number + 1):
        sum += i
    print(f"The sum of the integers between 1 and {number} is {sum}.")
elif operation == "p":
    product = 1
    for i in range(1, number + 1):
        product *= i
    print(f"The product of the integers between 1 and {number} is {product}.")