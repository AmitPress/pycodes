# time O(logN) and space O(logN)
from collections import defaultdict
def binsearch(arr, lo, hi, key):
    d = defaultdict()
    for i, val in enumerate(arr):
        d[val] = i
    arr.sort()
    while lo <= hi:
        mid = (lo+hi) // 2
        if arr[mid] == key:
            return d[arr[mid]]
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

a = [9, 3, 2, 4, 7, 2]
result_idx = binsearch(a, 0, len(a)-1, 2)
print(result_idx)