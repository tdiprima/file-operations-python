# Calculates and prints the Dice similarity coefficient (a statistical tool for comparing the similarity of two samples)
# between a segmented image and a ground truth image.
# https://stackoverflow.com/questions/31273652/how-to-calculate-dice-coefficient-for-measuring-accuracy-of-image-segmentation-i#31275008
import numpy as np

k = 1

# segmentation
seg = np.zeros((100, 100), dtype='int')
seg[30:70, 30:70] = k

# ground truth
gt = np.zeros((100, 100), dtype='int')
gt[30:70, 40:80] = k

dice = np.sum(seg[gt == k]) * 2.0 / (np.sum(seg) + np.sum(gt))
# data-post-id="48858111"
# dice = np.sum(seg[gt == k] == k) * 2.0 / (np.sum(seg[seg == k] == k) + np.sum(gt[gt == k] == k))

print('Dice similarity score is {}'.format(dice))
