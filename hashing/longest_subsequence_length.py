a = [5, 13, 6, 7, 1, 2, 14, 15, 3, 4, 8, 9, 12]


def countLeft(s, n):
    if n in s:
        s.remove(n)
        return 1 + countLeft(s, n - 1)
    return 0


def countRight(s, n):
    if n in s:
        s.remove(n)
        return 1 + countRight(s, n + 1)
    return 0


def find_max_subsequence_size(a):
    s = set(a)
    max = 0
    for n in a:
        count = 0
        if n in s:
            s.remove(n)
            count = count + 1
            count = count + countLeft(s, n - 1)
            count = count + countRight(s, n + 1)
        max = count if count > max else max
    print("ans is ", max)


find_max_subsequence_size(a)
