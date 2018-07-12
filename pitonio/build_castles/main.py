import csv


FILENAME = 'input.txt'


def read_data():
    with open(FILENAME) as f:
        reader = csv.reader(f)
        return [int(elem) for elem in next(reader)]


def solution(arr):
    total = 1  # the is always last segment where we can build a castle
    spike = 0

    prev = arr[0]
    for i in arr:
        if i == prev:
            continue

        if i > prev:
            if spike != 1:
                total += 1
            spike = 1

        if i < prev:
            if spike != -1:
                total += 1
            spike = -1

        prev = i

    return total


if __name__ == '__main__':
    print(solution(read_data()))
