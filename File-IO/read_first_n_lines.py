from itertools import islice
# https://stackoverflow.com/questions/1767513/read-first-n-lines-of-a-file-in-python

# TODO: BASH!
# head -n 501 fifa_data.csv > fluffit.csv

N = 100

with open("datafile") as my_file:
    head = [next(my_file) for x in range(N)]
print(head)

# or

with open("datafile") as my_file:
    head = list(islice(my_file, N))
print(head)

exit(0)
