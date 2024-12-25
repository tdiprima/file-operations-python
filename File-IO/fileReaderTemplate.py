import linecache
import os
import sys


def read_it(filename):
    with open(filename) as fp:
        for line in fp:
            # Do something with it
            print(line.rstrip())


read_it("some file")


def lookup(filename, lookup):
    '''
    Template
    :return:
    '''
    if not os.path.isfile(filename):
        print("File {} does not exist. Exiting...".format(filename))
        sys.exit()

    with open(filename) as fp:
        for line in fp:
            if lookup in line:
                print(line.rstrip())


# lookup('/Users/tdiprima/incep_mix_prob.out', 'docker exec')


def lookup_lineno(filename, lookup):
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            line = line.rstrip()
            if lookup in line and "Empty" not in line:
                print(linecache.getline(filename, (num - 7)).rstrip())
                print(linecache.getline(filename, (num - 6)).rstrip())
                print(linecache.getline(filename, (num - 5)).rstrip())
                print(linecache.getline(filename, (num - 4)).rstrip())
                print(linecache.getline(filename, (num - 3)).rstrip())
                print(linecache.getline(filename, (num - 2)).rstrip())
                print(linecache.getline(filename, (num - 1)).rstrip())
                print(line.rstrip())
                print()


# lookup('/Users/tdiprima/Desktop/Gleason/nohup.out', 'Error')


def modify_contents(filename):
    '''
    Template
    :return:
    '''

    if not os.path.isfile(filename):
        print("File path {} does not exist. Exiting...".format(filename))
        sys.exit()

    with open(filename) as fp:
        for line in fp:
            print(line.rstrip())


def extract_folder_name(filename):
    if not os.path.isfile(filename):
        print("File path {} does not exist. Exiting...".format(filename))
        sys.exit()

    with open(filename) as fp:
        for line in fp:
            line = line.rstrip()
            arr = line.split("/")
            folder = arr[len(arr) - 2]  # folder name
            current_file = arr[len(arr) - 1]  # file name
            file_extension = os.path.splitext(line)
            new_name = "meta_" + str(folder) + file_extension[1]
            print("cp -v " + line + " $HOME/" + new_name)


# extract_folder_name('files.list')


def fix_bridge(filename):
    '''
    1) find [folder] -name *.csv > ~/files.list
    2) Run this > copy_rename.sh
    '''
    if not os.path.isfile(filename):
        print("File path {} does not exist. Exiting...".format(filename))
        sys.exit()

    with open(filename) as fp:
        for line in fp:
            line = line.rstrip()
            arr = line.split("/")
            folder = arr[len(arr) - 2]  # folder name is unique name
            old_name = arr[len(arr) - 1]  # old name
            new_name = str(folder) + ".csv"
            # print("sudo cp -v " + old_name + " /data/tammy/pyrad_in/" + new_name)
            print("sudo cp -v " + line + " /data/tammy/pyrad_in/" + new_name)
    print("find /data/tammy/pyrad_in/ -type f | wc -l")


# fix_bridge('files.list')


def wordcount():
    '''
    MAIN
    https://stackabuse.com/read-a-file-line-by-line-in-python/
    :return:
    '''
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    bag_of_words = {}
    with open(filepath) as fp:
        cnt = 0
        for line in fp:
            print("line {} contents {}".format(cnt, line))
            record_word_cnt(line.strip().split(' '), bag_of_words)
            cnt += 1
    sorted_words = order_bag_of_words(bag_of_words, desc=True)
    print("Most frequent 10 words {}".format(sorted_words[:10]))


def order_bag_of_words(bag_of_words, desc=False):
    words = [(word, cnt) for word, cnt in bag_of_words.items()]
    return sorted(words, key=lambda x: x[1], reverse=desc)


def record_word_cnt(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1


def read_into_list():
    '''
    https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
    '''
    # Read it into a list
    with open('filename') as f:
        lines = f.readlines()
    # lines = [line.rstrip('\n') for line in open('filename')]


exit(0)

# if __name__ == '__main__':
#     main()
#     exit(0)
