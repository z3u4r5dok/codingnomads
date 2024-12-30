# Your cat just had kittens! Now you want to put up an ad to give them
# to your friends. You'll need to save all names of the kittens,
# confirm that they each of them is cute, and show a message that
# that kitten is ready for adoption.
#
# Break this task up into a couple of steps of pseudocode
# and write the pseudocode below in code comments.
# You don't need to write any functional code, just map out the steps.


# How many kittens did my cat had.
# Based on the amount of kittens then gather some friends names to propose or offer them in adoption
# Make sure those friends are not allergic and love kittens, to make sure, they'll want and take good care of them.
# Creata an add putting up all kitten's names and make sure they will look clean and appealing to the possible owner's kitten.
# Create a message stating that the kittens are in good health, and all have names and behave just waiting to being love and provide it as well.

""" Improve Pseudocode 

* More structured pseudocode: While we listed the steps, they could be more structured
and closer to actual pseucode conventions.

*Focus on the core requirements: The task specifically mentions saving kitten names,
 confirming cuteness, and showing an adoption message. These should be prominent in our
 pseudocode.

* Less about finding friends: The focus is on the ad and kittens, not finding friends (though it's 
  a pracitcal consideration)

Here's the improved version of the pseudocode:

# Create an empty list to store kitten names
SET kitten_names TO []

# Get the number of kittens
GET number_of_kittens

# Repeat the following steps for each kitten:
FOR each kitten in range(number_of_kittens):
    # GET the kitten's name
    GET kitten_name
    # Add the kitten's name to the list
    APPEND kitten_name TO kitten_names
    # Confirm the kitten is cute (this could be a human check, not code)
    CONFIRM kitten is cute
    # Display an adoption message for the kitten
    PRINT kitten_name + " is ready for adoption!"

# Create an ad with the list of kitten names
CREATE ad with kitten_names


Explanation of improvements:

Data structure: Uses a list (kitten_names) to store the names, which is a common way to 
handle collections of data in programming.

Loop: Uses a FOR loop to repeat steps for each kitten, making the code more efficient.
   
Core requirements: Explicitly includes getting names, confirming cuteness, and printing 
adoption messages.

Simplified ad creation: Doesn't go into detail about making the ad, as that's not the main 
focus of the pseudocode.

"""