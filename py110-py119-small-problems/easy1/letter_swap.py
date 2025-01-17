def swap_first_and_last(word):
    if len(word) <= 1:
        return word
    
    chars = list(word)
    chars[0], chars[-1] = chars[-1], chars[0]
    return ''.join(chars)

def swap(string):
    words = string.split(' ')
    return ' '.join([swap_first_and_last(word) for word in words])


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True