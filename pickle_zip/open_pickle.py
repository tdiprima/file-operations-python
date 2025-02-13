"""
serializes several types of data into a pickle file, reads back the data, prints it, and then deletes the file.
https://stackoverflow.com/questions/35067957/how-to-read-pickle-file#35068254
Copyright 2021 Tammy DiPrima
"""
import os
import pickle

PICKLE_FILE = 'pickle.dat'


def main():
    # append data to the pickle file
    add_to_pickle(PICKLE_FILE, 123)
    add_to_pickle(PICKLE_FILE, 'Hello')
    add_to_pickle(PICKLE_FILE, None)
    add_to_pickle(PICKLE_FILE, b'World')
    add_to_pickle(PICKLE_FILE, 456.789)
    # load & show all stored objects
    for item in read_from_pickle(PICKLE_FILE):
        print(repr(item))
    os.remove(PICKLE_FILE)


def add_to_pickle(path, item):
    with open(path, 'ab') as file:
        pickle.dump(item, file, pickle.HIGHEST_PROTOCOL)


def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass


def foo(my_file):
    import pandas as pd
    object = pd.read_pickle(r'models/FastWSI_vgg_bestVal.pkl')
    print(object)


if __name__ == '__main__':
    main()
