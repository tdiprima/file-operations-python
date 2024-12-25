"""
Calculates and prints the Dice similarity score between two images, used for measuring the accuracy of image segmentation.

Load images (mask with 1 and 0)
https://stackoverflow.com/questions/31273652/how-to-calculate-dice-coefficient-for-measuring-accuracy-of-image-segmentation-i#65261238
"""
import cv2
import numpy as np


# Dice similarity function
def dice(pred, true, k=1):
    intersection = np.sum(pred[true == k]) * 2.0
    _dice = intersection / (np.sum(pred) + np.sum(true))
    return _dice


# y_pred = cv2.imread('predictions/match.png')
# y_true = cv2.imread('ground_truth/match.png')
# dice_score = dice(y_pred, y_true, k=255)  # 255 in my case, can be 1
# print("Dice Similarity: {}".format(dice_score))

y_pred = cv2.imread('../images/asplit.png')  # predictions
y_true = cv2.imread('../images/asplit-2.png')  # ground_truth
dice_score = dice(y_pred, y_true, k=255)
print("Dice Similarity: {}".format(dice_score))
