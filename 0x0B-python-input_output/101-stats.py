#!/usr/bin/python3
'''A module that contains a function, print_the_stats'''


def print_the_stats(size, status_codes):
    '''The function that prints the statistics'''

    print("File size: {}".format(size))
    for i in sorted(status_codes):
        print("{}: {}".format(i, status_codes[i]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    the_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_the_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in the_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_the_stats(size, status_codes)

    except KeyboardInterrupt:
        print_the_stats(size, status_codes)
        raise
