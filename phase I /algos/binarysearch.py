
def binary_search(arr, src_num):
    
    start = 0
    end = len(arr) -1
    head = abs(start - end)//2

    if src_num == arr[0]:
        return 0
    elif src_num == arr[-1]:
        return len(arr) -1 

    while start is not end and start is not head:
        if src_num > arr[head]:
            start = head +1 
            end = len(arr) - 1
            head = start + abs(start - end)//2
        elif src_num < arr[head]:
            start = 0
            end = abs(head -1)
            head = abs(start - end)//2
        else:
            break

    if src_num == arr[head]:
        return head
    else:
        return -1
 

    print(start, end, head) 

arr = [2,3,4,5,6,7,8,12, 22]

print(binary_search(arr, 0))
