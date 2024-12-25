# Initializes a numpy array and sets all elements less than 10 to 0 and all elements above 10 to 1,
# both via direct assignment and list comprehension.
# https://stackoverflow.com/questions/28430904/set-numpy-array-elements-to-zero-if-they-are-above-a-specific-threshold
import numpy as np

a = np.array([2, 23, 15, 7, 9, 11, 17, 19, 5, 3])
print(a, type(a))
thresh = 10

# Apply threshold
a[a < 10] = 0  # Do below first
print(a, type(a))  # verify
a[a > 10] = 1  # Then above
print(a, type(a))  # there you go!


def list_comp():
    # list comprehensions are faster than for loops in python
    a = np.array([2, 23, 15, 7, 9, 11, 17, 19, 5, 3])
    a = [0 if a_ > thresh else a_ for a_ in a]
    print(a, type(a))

    # cast to array
    a = np.array(a)
    print(a, type(a))
