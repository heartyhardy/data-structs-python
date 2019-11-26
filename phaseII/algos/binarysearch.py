
def binarysearch(arr, src):

    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == src:
            return mid
        elif arr[mid] > src:
            r = mid - 1
        else:
            l = mid + 1
    return -1


arr = [1,4,5,6,7,8,9,10]
print(binarysearch(arr, 0))
print(binarysearch(arr, 11))
print(binarysearch(arr, 4))
print(binarysearch(arr, 7))
print(binarysearch(arr, 9))

