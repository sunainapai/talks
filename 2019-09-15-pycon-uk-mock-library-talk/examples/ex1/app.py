# app.py

import sys
from os.path import getsize


def get_total_size(filenames):
    total = 0
    for f in filenames:
        total += getsize(f)
    return total


if __name__ == '__main__':
    args = sys.argv[1:]
    print(get_total_size(args))
