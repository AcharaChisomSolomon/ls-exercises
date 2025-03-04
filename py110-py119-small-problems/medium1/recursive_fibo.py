def fibonacci(num, memo={1: 1, 2: 1}):
    if memo.get(num):
        return memo[num]
    
    if num <= 2:
        return memo[num]
    
    value = fibonacci(num - 1) + fibonacci(num - 2)
    memo[num] = value
    return value

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
