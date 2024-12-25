# Loads prediction and truth values from files in provided directories, processes them by applying a threshold
# and checking for zero arrays, then calculates and outputs the Dice similarity scores for three grades
# ('Grade3', 'Grade4+5', 'Benign').
import os
import sys

import numpy as np
from scipy.spatial.distance import dice


def apply_threshold(arr):
    arr[arr < 0.5] = 0  # Do below first
    arr[arr >= 0.5] = 1  # Then above
    return arr


def is_all_zeros(arr):
    if np.any(arr):
        return False
    return True


def mask(arr):
    # x_loc = arr[:, 0]
    # y_loc = arr[:, 1]
    grade3 = arr[:, 2]
    grade4_5 = arr[:, 3]
    benign = arr[:, 4]

    # apply threshold
    grade3 = apply_threshold(grade3)
    grade4_5 = apply_threshold(grade4_5)
    benign = apply_threshold(benign)

    message = "Can't do it if the array is all zeros"
    if is_all_zeros(grade3):
        print(message, 'grade3')

    if is_all_zeros(grade4_5):
        print(message, 'grade4_5')

    if is_all_zeros(benign):
        print(message, 'benign')

    return grade3, grade4_5, benign


# Dice similarity function
def compute_dice(prediction, truth):
    try:
        similarity = 1.0 - dice(prediction.astype(bool), truth.astype(bool))
    except ZeroDivisionError:
        similarity = 0
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    return similarity


def compute1(prediction, truth, k=1):
    intersection = np.sum(prediction[truth == k]) * 2.0
    _dice = intersection / (np.sum(prediction) + np.sum(truth))
    return _dice


def process(fname, f_pred, f_true):
    y_pred = np.loadtxt(f_pred, skiprows=1).astype(np.float32)
    y_true = np.loadtxt(f_true, skiprows=1).astype(np.float32)
    if y_true.shape != y_pred.shape:
        print('The dimensions of the two sets are not equal', fname)
        exit(1)

    grade3A, grade4_5A, benignA = mask(y_pred)
    grade3B, grade4_5B, benignB = mask(y_true)

    score1 = compute_dice(grade3A, grade3B)
    score2 = compute_dice(grade4_5A, grade4_5B)
    score3 = compute_dice(benignA, benignB)
    print('{0},{1},{2},{3}'.format(fname, score1, score2, score3))


if __name__ == '__main__':
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    print("Dice Similarity")
    print("Slide,Grade3,Grade4+5,Benign")
    for dirName, subdirList, fileList in os.walk(folder1):
        for fname in fileList:
            if fname.startswith('prediction'):
                path1 = os.path.join(folder1, fname)
                path2 = os.path.join(folder2, fname)
                process(fname, path1, path2)
