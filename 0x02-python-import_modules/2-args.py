#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    size = len(argv) - 1
    if size == 1:
        print("{:d} argument:".format(size))
    elif size == 0:
        print("{:d} arguments.".format(size))
    else:
        print("{:d} arguments:".format(size))
    for i in range(0, len(argv)):
        if i > 0:
            print("{:d}: {:s}".format(i, argv[i]))
