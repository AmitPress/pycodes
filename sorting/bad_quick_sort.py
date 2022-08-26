# https://opendsa-server.cs.vt.edu/embed/quicksortAV

import random 
random_data = [random.randint(1, i+1) for i in range(1024)]
data = [1, -1, 5, 4, 0]

def partition(arr, lo, hi):
    pivot = lo
    i = lo
    j = hi
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, lo, hi):
    if lo<hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p+1, hi)
quicksort(data, 0, len(data)-1)
print(data)