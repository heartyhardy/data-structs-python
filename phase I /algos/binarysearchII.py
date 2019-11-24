def binarysearch(arr, src):
    start = 0
    end = len(arr) -1

    while start <= end:
        head = start + (end - start) // 2

        if arr[head] == src:
            return head
        elif arr[head] < src:
            start = head + 1
        else:
            end = head - 1
        
    return -1

arr = [1, 2, 3, 5, 7, 10]
print(binarysearch(arr, 4))
print(binarysearch(arr, 2))
print(binarysearch(arr, 10))
print(binarysearch(arr, 15))