num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")
num3 = input("Enter the 3rd number: ")
num4 = input("Enter the 4th number: ")
num5 = input("Enter the 5th number: ")
search_num = input("Enter the last number: ")
print()

nums = [num1, num2, num3, num4, num5]
if search_num in nums:
    print(f"{search_num} is in {','.join(nums)}.")
else:
    print(f"{search_num} isn't in {','.join(nums)}.")