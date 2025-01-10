def calculate_grade(score):
    grade = 'F'

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'

    return grade

def get_average(a, b, c):
    return (a + b + c) / 3

def get_grade(a, b, c):
    return calculate_grade(get_average(a, b, c))


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True