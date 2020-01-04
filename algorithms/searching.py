def unsortedsearch(item, arr): # Brute force O(n)
    i = 0
    while i < len(arr) and arr[i] != item:
        i += 1

    if i < n:
        return i
    else:
        return -1

def binarysearch(item, arr, left, right): # RECURSION O(log(n))
    if right - left == 0:
        return False
    
    mid = (left + right) / 2
    if item == arr[mid]:
        return True         # Base case
    
    if item < arr[mid]:
        return binarysearch(item, arr, left, mid)
    else:  
        return binarysearch(item, arr, mid+1, right)


