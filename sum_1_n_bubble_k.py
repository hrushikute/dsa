def bubbleSort(arr, k):
    """
    argument arr is list, k is int
    store result in res
    """

    res = 0
    # YOUR CODE GOES HERE
    for i in range(k):
        for j in range(i+1,k):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
        print(arr)
    print((arr[0]+arr[-1]))

    return res

bubbleSort([64, 34, 25, 12, 22, 11, 90],4)