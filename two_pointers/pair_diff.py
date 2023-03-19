# Given a sorted array a[] and difference k, find index i and j such that a[j]-a[i]=k.
a = [1,4,5,7,8,11]


def find_diff(a, k):
    i = 0
    j = 1
    while i < len(a) and j < len(a):
        if a[j]-a[i] == k:
            return a[i], a[j]
        elif a[j] - a[i] > k:
            i = i+1
        else:
            j = j+1

print(find_diff(a,2))