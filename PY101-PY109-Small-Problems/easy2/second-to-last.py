def penultimate(sentence):
    words = sentence.split(" ")
    return words[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")