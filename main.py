def insertionSort(arr, k):
    """
    arr is the list and k is the iteration number
    store the result with variable name res
    """
    # YOUR CODE GOE;S HERE
    # if len(arr)==0:
    #     return None
    counter =0
    res=None
    for i in range(1,len(arr)):
        el=arr[i]

        j = i-1
        while j>=0 and arr[j]>el and counter <k:
            arr[j+1]=arr[j]
            j-=1
        counter+=1
        arr[j+1]=el
        print(arr,counter)
        if i>=k:
            res = arr[len(arr)//2]
            break
    print(arr,res)
    return res

insertionSort([111 ,123 ,435 ,23 ,100, 101 ,540 ,1000],5)
insertionSort([12, 4, 5, 7, 1, 32, 34],4)