#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    argv_len = len(argv[1:])
    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{argv_len} arguments:")
        for i in range(1, argv_len + 1):
            print(f"{i}: {argv[i]}")
