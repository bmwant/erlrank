def solution(n):
    n_copy = n
    d = [0] * 30  # binary repr of a number will be stored here
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1

    binary_repr = '{0:b}'.format(n_copy)
    binary_repr2 = ''.join([str(elem) for elem in d])
    binary_repr3 = ''.join(reversed([str(elem) for elem in d]))
    print(binary_repr, len(binary_repr))
    print(binary_repr2, l)

    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


if __name__ == '__main__':
    n = 955
    # n = 1_000_000_000
    print(solution(n))
