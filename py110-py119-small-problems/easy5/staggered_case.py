def staggered_case(string):
    output = ''

    for i in range(len(string)):
        char = string[i]

        if char.isalpha():
            if i % 2 == 0:
                output += char.upper()
            else:
                output += char.lower()
        else:
            output += char

    return output


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True