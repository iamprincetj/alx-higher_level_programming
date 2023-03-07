#!/usr/bin/python3

for num in range(0, 100):
    if num < 10:
        num = '0' + str(num)
    if num != 99:
        print(num, end=", ")
    else:
        print(num)
