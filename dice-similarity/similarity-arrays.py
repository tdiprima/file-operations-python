# Calculates and prints the similarity between two vectors using the Dice Coefficient.
# https://vinta.ws/code/calculate-the-similarity-of-two-vectors.html
import numpy as np
from scipy.spatial.distance import dice

v1 = np.array([1, 2, 3, 4])
v2 = np.array([1, 2, 3, 4])

try:
    # 1 - dice(a, b) CALCULATES SIMILARITY!
    sim = 1.0 - dice(v1.astype(bool), v2.astype(bool))
except ZeroDivisionError:
    sim = 0

print('sim', sim)
