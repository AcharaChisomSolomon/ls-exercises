def center_of(sentence):
    length = len(sentence)

    if length % 2 == 1:
        id = ((length - 1) // 2)
        return sentence[id]
    else:
        id = length // 2
        return sentence[id - 1:id + 1]
    

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True