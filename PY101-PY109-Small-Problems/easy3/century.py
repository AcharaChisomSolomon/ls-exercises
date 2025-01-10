def get_century(year):
    century = year // 100
    return century + 1 if str(year)[-1] != '0' else century

def add_suffix(century):
    century = str(century)
    last_char = century[-1]

    if len(century) >= 2:
        if century[-2] == '1':
            return f"{century}th"

    if last_char == '1':
        century += 'st'
    elif last_char == '2':
        century += 'nd'
    elif last_char == '3':
        century += 'rd'
    else:
        century += 'th'

    return century

def century(year):
    return add_suffix(get_century(year))

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True