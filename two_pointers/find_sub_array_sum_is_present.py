# Given an array a and sum k, find if sub subarray exist such that the sum of the sub array is k.

a = [1,4,5,7,8,11]


def calculate_psa(a):
    for i in range(1,len(a)):
        a[i] = a[i-1]+a[i]


def get_subarray_sum(i,j):
    if i == 0:
        return a[j]
    else:
        return a[j]-a[i-1]


def find_subarray(a,k):
    calculate_psa(a)
    i,j = 0,1
    while i < len(a) and j < len(a):
        sas = get_subarray_sum(i, j)
        if k == sas:
            return i, j
        elif sas > k:
            i = i+1
        else:
            j= j+1


print(find_subarray(a, 21))

