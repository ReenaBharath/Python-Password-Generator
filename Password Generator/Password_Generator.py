import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here
uppercaseLetter1 = chr(random.randint(65, 90)) 
uppercaseLetter2 = chr(random.randint(65, 90)) 
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
number = chr(random.randint(48, 57))
symbol = chr(random.randint(33, 47))

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number + symbol + lowercaseLetter1 + symbol
password = shuffle(password)

# Output
print(password)
