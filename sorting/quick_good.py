# this is the hooare algorithm that is down below

# we need a random partition point

def get_partition(arr, lo, hi):
    mid = (lo+hi)//2
    pivot = hi
    # get the second largest or second smallest number from a 3 sized array (get the median(middle value) of 3)
    if arr[lo]<arr[mid]:
        if arr[mid]<arr[hi]:
            pivot = mid
    elif arr[lo]<arr[hi]:
        pivot = lo
    return pivot
def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def partition(arr, lo, hi):
    pivot = get_partition(arr, lo, hi)
    swap(arr, pivot, hi)
    for i in range(lo, hi):
        if arr[i]<=arr[hi]:
            swap(arr, i, lo)
            lo += 1
    swap(arr, lo, hi)
    return lo

def QuickSort(arr, lo, hi):
    if lo<hi:
        p = partition(arr, lo, hi)
        QuickSort(arr, lo, p-1)
        QuickSort(arr, p+1, hi)

import random
ary = [random.randint(i, i+1) for i in range(100, 0, -1)]
print(ary)
QuickSort(ary, 0, len(ary)-1)
print('-----------------------------------------')
print(ary)