"""
Calculates and prints the Dice dissimilarity index between various pairs of 3-element binary and integer arrays
using Scipy's 'dice' function.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.dice.html
"""
from scipy.spatial import distance

print("Dissimilarity index:")
print(distance.dice([1, 0, 0], [0, 1, 0]))
print(distance.dice([1, 0, 0], [1, 1, 0]))
print(distance.dice([1, 0, 0], [2, 0, 0]))
# print(distance.dice([0, 0, 0], [0, 0, 0]))  # They can't be all zeros.
print(distance.dice([1, 1, 1], [1, 1, 1]))
