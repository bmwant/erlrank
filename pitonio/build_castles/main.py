import csv


FILENAME = 'input.txt'


def read_data():
    with open(FILENAME) as f:
        reader = csv.reader(f)
        return [int(elem) for elem in next(reader)]

# arr = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
DATA = [0, 1, 1, 2]
# DATA = [1, 0, 1]
# DATA = [0, 1, 0]


def solution(arr):
    count_castles = 0
    bottom_castle = True
    top_castle = False

    if len(arr) == 1:
        return 1

    # handle first section
    if arr[0] > arr[1]:
        # inverse logic when starting from top
        bottom_castle = False
        top_castle = True

    prev = arr[0]
    # without a arr[1:-1] slice to be memory efficient
    for i in arr:
        if i == prev:
            continue

        if i > prev:
            if bottom_castle:
                count_castles += 1
            bottom_castle = False
            top_castle = True
            prev = i
            continue

        if i < prev:
            if top_castle:
                count_castles += 1
            bottom_castle = True
            top_castle = False
            prev = i
            continue

    # handle last section
    if arr[-1] != arr[-2]:
        count_castles += 1

    # the terrain is flat so at least one castle can be built
    return count_castles or 1



if __name__ == '__main__':
    print(solution(DATA))
