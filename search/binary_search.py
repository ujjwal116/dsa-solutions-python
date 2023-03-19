def b_search(a, n):
    l, h = 0, len(a) - 1

    while h >= l:
        mid = (l + h) // 2
        if n == a[mid]:
            return mid
        elif n < a[mid]:
            h = mid - 1
        else:
            l = mid + 1


def search(a, n):
    print(b_search(a, n))


# a = [1, 4, 6, 7, 9, 23, 45]
# n = 45
# search(a, n)
