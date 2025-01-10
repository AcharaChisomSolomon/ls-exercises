def replace_non_alphabetic_char(sentence):
    for char in sentence:
        if not char.isalpha():
            sentence = sentence.replace(char, ' ')
    return sentence

def remove_duplicate_space(sentence):
    output = sentence[0]

    for char in sentence:
        if char == ' ' and output[-1] == ' ':
            continue
        output += char

    return output

def clean_up(sentence):
    return remove_duplicate_space(replace_non_alphabetic_char(sentence))


print(clean_up("---what's my +*& line?") == " what s my line ") # True