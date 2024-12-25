"""
https://www.sharpsightlabs.com/blog/numpy-load/
Load Numpy arrays from Numpy storage files
Copyright 2021 Astro Pup
"""
from numpy import load


def f1(f):
    # data = load('out.npz')
    data = load(f)  # f, allow_pickle=True
    lst = data.files
    for item in lst:
        print(item)
        print(data[item])


def f2(f):
    with load(f) as data:
        # key_real, key_score, key_pred, key_namelist
        a = data['key_namelist']  # some file in the archive
        print(a)


if __name__ == '__main__':
    mf = 'results/test_pred_score.npz'
    f1(mf)
    # f2(mf)
