def remove_non_letters(word):
    return ''.join([char for char in list(word) if char.isalpha()])

def word_sizes(string):
    output = {}

    if len(string) == 0:
        return output
    
    words = string.split(' ')
    words = [remove_non_letters(word) for word in words]

    for word in words:
        if len(word) in output:
            output[len(word)] = output[len(word)] + 1
        else:
            output[len(word)] = 1

    return output

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})