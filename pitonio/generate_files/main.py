from string import printable
from random import choice, randint


FILES_NUMBER = 100
MIN_LINE_LENGTH = 1
MAX_LINE_LEGTH = 65


def get_content_by_number(number, buffer):
    if number % 7 == 0:
        content = buffer
    elif number % 5 == 0:
        content = 'This is every 5th file!'
    else:
        line_length = randint(MIN_LINE_LENGTH, MAX_LINE_LEGTH)
        content = ''.join([choice(printable) for _ in range(line_length)])

    return content


def main():
    CONCTENATED_BUFFER = ''
    for file_index in range(FILES_NUMBER):
        file_number = file_index + 1
        file_content = get_content_by_number(file_number, CONCTENATED_BUFFER)
        CONCTENATED_BUFFER += file_content
        filename = 'file{:02d}.txt'.format(file_number)
        with open(filename, 'w') as f:
            f.write(file_content)


if __name__ == '__main__':
    main()
