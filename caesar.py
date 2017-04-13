import string

def alphabet_position(letter):
    if letter in string.ascii_lowercase:
        return string.ascii_lowercase.find(letter)
    elif letter in string.ascii_uppercase:
        return string.ascii_uppercase.find(letter) % 26
    else:
        return None
#tests
#print(alphabet_position("a"))
#print(alphabet_position("E"))
#print(alphabet_position("!"))

def rotate_character(char, rot):
    if char in string.ascii_letters:
        newposition = int(string.ascii_letters.find(char)) + int(rot)
        if newposition <= 26:
            position = string.ascii_letters[newposition]
            if char in string.ascii_uppercase:
                return position.upper()
            else:
                return position.lower()
        else:
            newUpperposition = newposition % 26
            position = string.ascii_letters[newUpperposition]
            if char in string.ascii_uppercase:
                return position.upper()
            else:
                return position.lower()
    else:
        return char
#tests
#print(rotate_character("a", 1))
#print(rotate_character("E", 2))
#print(rotate_character("y", 3))
#print(rotate_character("Z", 2))
#print(rotate_character("!", 2))

def lettersonly(text): #function created to help figure out the needed length of the key string
    lettersonly = []
    for char in text:
        if char.isalpha():
            lettersonly.append(char)
    return ''.join(lettersonly)

def encrypt(text, rot):
    newstring = ""
    for letter in text:
        newletter = rotate_character(letter, rot)
        newstring += str(newletter)
    return newstring
