#!/usr/bin/env python3

"""Python code to get difference of two lists.
https://www.geeksforgeeks.org/python-difference-two-lists/
"""

import sys


def diff(li1, li2):
    print('len li1', len(li1))
    print('len li2', len(li2))
    result = list(set(li1) - set(li2)) + list(set(li2) - set(li1))
    print('len result', len(result))
    return result


def main(arguments):
    # Driver Code
    li1 = ['--highlight', '--bg-dark', '--bg-dark1', '--bg-dark-top', '--text-dark', '--text-secondary', '--hover-dark',
           '--border-dark', '--primary-dark', '--bg-light', '--bg-light1', '--text-light', '--text-important',
           '--border-light', '--primary-light', '--secondary-light', '--sun', '--tooltip', '--no-frills', '--rgb-on',
           '--rgba-on']
    li2 = ['--text-light', '--bg-light', '--text-dark', '--bg-dark', '--sun', '--highlight', '--no-frills', '--rgb-on',
           '--rgba-on', '--tooltip']
    print(diff(li1, li2))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
