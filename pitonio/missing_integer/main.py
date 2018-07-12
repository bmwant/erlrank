import csv


FILENAME = 'input.txt'


def read_data():
    with open(FILENAME) as f:
        reader = csv.reader(f)
        return [int(elem) for elem in next(reader)]


def solution(arr):
    size = len(arr)
    markers = [0] * size
    for elem in arr:
        if 0 < elem <= size:
            markers[elem-1] = 1

    for i, value in enumerate(markers, 1):
        if value == 0:
            return i
    # return max positive element plus one
    return i + 1


if __name__ == '__main__':
    arr = read_data()
    print(solution(arr))
