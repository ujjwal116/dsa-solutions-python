def merge(arr, left, mid, right):
    la = arr[left:mid+1]
    ra = arr[mid+1:right+1]
    k = left
    i = 0
    j = 0
    while k <= right:
        if i == len(la) or j == len(ra):
            break
        if la[i] < ra[j]:
            arr[k] = la[i]
            i = i+1
        else:
            arr[k] = ra[j]
            j = j+1
        k = k+1

    if i != len(la):
        for x in range(k, right + 1):
            arr[x] = la[i]
            i = i+1

    if j != len(ra):
        for x in range(k, right+1):
            arr[x] = ra[j]
            j = j+1


def merge_sort(arr, left, right):
    if right > left:
        mid = (right + left)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


arr1 = [25, 5, 5, 7, 34, 31]
merge_sort(arr1, 0, 5)
print(arr1)
