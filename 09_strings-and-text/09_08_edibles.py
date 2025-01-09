# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."


fruit = s[5:9] + s[11]
poultry = s[25:29] + s[31]
ingredient_0 = s[57:63]
dough = s[68:73]

recipe = fruit + " " + poultry + " " + ingredient_0 + " " + dough
print(recipe)
