#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv)
args = sys.argv
count = 1
if length == 1:
    print("{} arguments.".format(length - 1))
else:
    print("{} arguments:".format(length - 1))
while length > 1:
    for i in args:
        if count <= length - 1:
            print("{}: {}".format(count, args[count]))
            count = count + 1
        else:
            exit()
