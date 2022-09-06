def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    return merge(left,right)


def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    result = []

    i, j = 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    if i < n1:
        result += arr1[i:]

    if j < n2:
        result += arr2[j:]

    return result

print(merge_sort([3, 4, 5 ,2,8,1]))