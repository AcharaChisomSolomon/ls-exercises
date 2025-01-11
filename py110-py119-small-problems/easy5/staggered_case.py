def staggered_case(string):
    output = ''
    i = 0

    for char in string:
        if char.isalpha():
            if i % 2 == 0:
                output += char.upper()
            else:
                output += char.lower()
            i += 1
        else:
            output += char

    return output


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True