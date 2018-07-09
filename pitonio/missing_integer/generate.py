import csv
import random


FILENAME = 'input01.txt'


def write_data(arr):
    with open(FILENAME, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(arr)


def generate():
    arr = list(range(1, 40_001))
    random.shuffle(arr)
    write_data(arr)


if __name__ == '__main__':
    generate()
