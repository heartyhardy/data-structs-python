def bubblesort(arr):
    maxpos = len(arr) - 1
    pos = 0

    while maxpos >= 0:
        if arr[pos] > arr[pos+1]:
            l = arr[pos]
            r = arr[pos+1]
            arr[pos] = r
            arr[pos+1] = l
        pos += 1

        if pos >= maxpos -1:
            maxpos -= 1
            pos=0

    return arr

arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubblesort(arr))