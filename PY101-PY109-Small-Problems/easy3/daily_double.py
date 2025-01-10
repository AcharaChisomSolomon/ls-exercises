def crunch(sentence):
    if sentence == '': return ''

    output = sentence[0]

    for char in sentence:
        if output[-1] == char:
            continue
        output += char

    return output

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')