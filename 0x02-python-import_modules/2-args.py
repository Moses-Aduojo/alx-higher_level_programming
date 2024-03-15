#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        if len(argv) == 2:
            print("{} argument:".format(len(argv) - 1))
        else:
            print("{} arguments:".format(len(argv)))
        for i in range(1, (len(argv))):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments.".format(0))
