"""
Calculates and prints the Dice coefficient, a similarity measure between two boolean NumPy arrays,
also providing functionality to generate random boolean masks.

1. https://gist.github.com/JDWarner/6730747
2. https://gist.github.com/brunodoamaral/e130b4e97aa4ebc468225b7ce39b3137
"""
import numpy as np


def dice(im1, im2, empty_score=1.0):
    """
    Computes the Dice coefficient, a measure of set similarity.

    Parameters
    ----------
    empty_score: In case of both inputs being zero, return 1.0
    im1 : array-like, bool
        Any array of arbitrary size. If not boolean, will be converted.
    im2 : array-like, bool
        Any other array of identical size. If not boolean, will be converted.

    Returns
    -------
    dice : float
        Dice coefficient as a float on range [0,1].
        Maximum similarity = 1
        No similarity = 0
        Both are empty (sum eq to zero) = empty_score

    Notes
    -----
    The order of inputs for `dice` is irrelevant. The result will be
    identical if `im1` and `im2` are switched.

    """
    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    im_sum = im1.sum() + im2.sum()
    if im_sum == 0:
        return empty_score

    # Compute Dice coefficient
    intersection = np.logical_and(im1, im2)

    return 2. * intersection.sum() / im_sum


def make_random_mask():
    # Faster
    a = np.zeros(10000, dtype=int)  # create array of integer zeros
    a[:1000] = 1  # set first 1000 to 1
    np.random.shuffle(a)  # shuffle!
    a = a.astype(bool)  # cast to bool
    return a


def make_random_mask1():
    a = np.full(10000, False)  # create array of false values
    a[:1000] = True  # set first 1000 to true
    np.random.shuffle(a)  # shuffle!
    return a


if __name__ == '__main__':
    img1 = make_random_mask()
    # img2 = make_random_mask()
    # score = dice(img1, img2)
    score = dice(img1, img1)
    print('score:', score)
