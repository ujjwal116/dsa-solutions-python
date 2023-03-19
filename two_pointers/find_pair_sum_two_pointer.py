# given an array a[]  and number k find i and such that a[i] + a[j] = k
def pair_sum(a,k):
    i=0
    j=len(a)-1
    while i != j:
        if (a[i] +a[j]) == k:
            # print(i, j)
            return a[i], a[j]
        elif (a[i] + a[j]) < k:
            i = i+1
        else:
            j = j-1


a = [2, 4, 5, 8, 9, 11, 13, 21]
print(pair_sum(a,19))
