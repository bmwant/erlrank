from main import solution


CASES = (
    ([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5], 4),
    ([0, 1, 1, 2], 2),
    ([1, 0, 1], 3),
    ([0, 1, 0], 3),
    ([0, 1, 1, 0, 0], 3),
    ([0, 0, 1, 1, 0, 0], 3),
    ([1, 1, 1, 1, 1, 1], 1),
    ([5, 4, 3, 2, 1, 0], 2),
    ([2, 4, 6, 8], 2),
)


def run_tests():
    errors = 0
    total_cases = len(CASES)
    for (i, (test_data, correct_result)) in enumerate(CASES):
        result = solution(test_data)
        if result != correct_result:
            print('Expected {}, got {}. Case #{}: {}'.format(
                correct_result, result, i, test_data))
            errors += 1

    if errors:
        print('Solution failed on {} test cases'.format(errors))
    else:
        print('All tests passed ({}/{})'.format(total_cases, total_cases))


if __name__ == '__main__':
    run_tests()
