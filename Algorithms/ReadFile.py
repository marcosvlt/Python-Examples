"""

How to read a txt file in python

"""

try:
    with open('file.txt', 'r') as file:
        for line in file:
            print(line)
except IOError:
    print("An Error Ocurried. Please verify file patch")


