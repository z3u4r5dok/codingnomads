# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

'''
print(word[1::4])
print(word[-2])
print(word[2:4])
print(word[0])
print(word[-3])
print(word[2:4])
print(word[-2])
'''

name1 = word[1::4]

name2 = word[-2] + word[2:4]

name3 = word[0] + word[-3] + word[2:4] + word[-2]

print(name1 + " " + name2 + " " + name3)