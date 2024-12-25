# Generates two random binary tensors, then calculates and prints the mean Dice coefficient between
# corresponding channels using single_dice_coef function, and Dice coefficient over the entire volume
# using the dice_coef2 function.

import numpy as np

np.random.seed(0)
true = np.random.rand(10, 5, 5, 4) > 0.5
pred = np.random.rand(10, 5, 5, 4) > 0.5


def single_dice_coef(y_true, y_pred_bin):
    # shape of y_true and y_pred_bin: (height, width)
    intersection = np.sum(y_true * y_pred_bin)
    if (np.sum(y_true) == 0) and (np.sum(y_pred_bin) == 0):
        return 1
    return (2 * intersection) / (np.sum(y_true) + np.sum(y_pred_bin))


def mean_dice_coef(y_true, y_pred_bin):
    # shape of y_true and y_pred_bin: (n_samples, height, width, n_channels)
    batch_size = y_true.shape[0]
    channel_num = y_true.shape[-1]
    mean_dice_channel = 0.
    for i in range(batch_size):
        for j in range(channel_num):
            channel_dice = single_dice_coef(y_true[i, :, :, j], y_pred_bin[i, :, :, j])
            mean_dice_channel += channel_dice / (channel_num * batch_size)
    return mean_dice_channel


def dice_coef2(y_true, y_pred):
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    union = np.sum(y_true_f) + np.sum(y_pred_f)
    if union == 0: return 1
    intersection = np.sum(y_true_f * y_pred_f)
    return 2. * intersection / union


print(mean_dice_coef(true, pred))
print(dice_coef2(true, pred))

# 0.4884357140842496
# 0.499001996007984
