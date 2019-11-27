
"""
Need to traverse through array and search for items which sums up to T

case 1: T = 20 arr = [2, 5, 7, 14, 15] YES
case 2: T = 25 arr = [2, 3, 5, 6, 7] NO

Assumptions:
1. Array is sorted
2. Array is not empty
3. Array contains intergers

"""


"""
Pseudocode

start = 0
end = array.length
T = target sum

if(arr.length < 2)
    return
if(arr[last_element] + arr[last_element-1] < T)
    return // Sum does not exist
else if(arr[first_element] + arr[second_element] > T)
    return // Sum doesnt exist

while l < r
    if arr[l] + arr[r] equals Sum
        return l,r
    else if arr[l] + arr[r] > Sum:
        r = r - 1
    else if arr[l] + arr[r] < Sum:
        l = l + 1

"""

"""
Implement the first part
"""

def sumoftwo(arr, sum):
    l = 0
    r = len(arr)-1

    if len(arr) < 2:
        return

    if (arr[0] + arr[1]) > sum:
        return
    elif (arr[-1] + arr[-2]) < sum:
        return

    
    while l < r:
        if arr[l] + arr[r] == sum:
            return l, r
        elif arr[l] + arr[r] < sum:
            l += 1
        elif arr[l] + arr[r] > sum:
            r -= 1

