import find_pair_sum_two_pointer


# find i,j,k in such a way that a[i]+a[j]+a[k]=sum
def find_tri(a, s):
    for i in range(len(a)):
        arr = a[:i] + a[i + 1:]
        ans = find_pair_sum_two_pointer.pair_sum(arr, s - a[i])
        if ans is not None:
            print(ans, a[i])


find_tri([1, 3, 5, 8, 9, 12], 23)
