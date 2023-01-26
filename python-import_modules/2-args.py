#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv) - 1
args = sys.argv
count = 1
if length == 0:
    print("{} arguments.".format(length))
elif length == 1:
    print("{} argument:".format(length))
else:
    print("{} arguments:".format(length))
while length > 0:
    for i in args:
        if count <= length:
            print("{}: {}".format(count, args[count]))
            count = count + 1
        else:
            exit()
