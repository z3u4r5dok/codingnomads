# Write the necessary code to print the BIG PYTHON string shown below.
# Research multi-line strings to make this easier for you :)
#
#     PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
#     P   P   Y   Y       T      H    H     O O    N N     N
#     P   P    Y Y        T      H    H    O   O   N  N    N
#     PPPP      Y         T      HHHHHH    O   O   N   N   N
#     P         Y         T      H    H    O   O   N    N  N
#     P         Y         T      H    H     O O    N     N N
#     P         Y         T      H    H      O     N       N




'''
To generate the "BIG PYTHON" output pattern programmatically, we can write a Python script 
that uses a list of strings to define each row of the letters and then prints them in the required format.
'''

# Define the rows for each letter in "PYTHON"


P = [
    " PPPP  ",
    " P   P ",
    " P   P ",
    " PPPP  ",
    " P     ",
    " P     ",
    " P     "
]

Y = [
    " Y     Y ",
    "  Y   Y  ",
    "   Y Y   ",
    "    Y    ",
    "    Y    ",
    "    Y    ",
    "    Y    "
]

T = [
    " TTTTTTTTT ",
    "     T     ",
    "     T     ",
    "     T     ",
    "     T     ",
    "     T     ",
    "     T     "
]

H = [
    " H    H ",
    " H    H ",
    " H    H ",
    " HHHHHH ",
    " H    H ",
    " H    H ",
    " H    H "
]

O = [
    "   O   ",
    "  O O  ",
    " O   O ",
    " O   O ",
    " O   O ",
    "  O O  ",
    "   O   "
]

N = [
    " N       N ",
    " N N     N ",
    " N  N    N ",
    " N   N   N ",
    " N    N  N ",
    " N     N N ",
    " N       N "
]

# Combine the letters to form "PYTHON"
big_python = zip(P, Y, T, H, O, N)

# Print the output line by line
for row in big_python:
    print("".join(row))



'''
 Row-by-row construction approach instead of predefining individual letters as separate lists. 
 This involves defining each row of the entire output manually based on the pattern of the letters.
 '''
# Define each row of the output for "BIG PYTHON"
rows = [
    "#     PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N",
    "#     P   P   Y   Y       T      H    H     O O    N N     N",
    "#     P   P    Y Y        T      H    H    O   O   N  N    N",
    "#     PPPP      Y         T      HHHHHH    O   O   N   N   N",
    "#     P         Y         T      H    H    O   O   N    N  N",
    "#     P         Y         T      H    H     O O    N     N N",
    "#     P         Y         T      H    H      O     N       N"
]

# Print each row
for row in rows:
    print(row)


'''
Using a multi-line string (""" """ or ''' ''') to directly define the desired pattern. 
This approach minimizes logic and code complexity since we simply store the output as a string and print it.
'''

# Define the pattern as a single multi-line string
big_python = """
#     PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
#     P   P   Y   Y       T      H    H     O O    N N     N
#     P   P    Y Y        T      H    H    O   O   N  N    N
#     PPPP      Y         T      HHHHHH    O   O   N   N   N
#     P         Y         T      H    H    O   O   N    N  N
#     P         Y         T      H    H     O O    N     N N
#     P         Y         T      H    H      O     N       N
"""

# Print the pattern
print(big_python)
