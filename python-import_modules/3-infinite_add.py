#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv) - 1
position = 1
add = 0
while length >= position:
    if length == 0:
        print("{}".format(0))
    add = add + int(sys.argv[position])
    position = position + 1
print("{}".format(add))
