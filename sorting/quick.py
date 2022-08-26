import random 
random_data = [random.randint(1, i+1) for i in range(65536)]
data = [8, -1, 1, -3, 7, 0, -7, 5]

def get_pivot(arr, lo, hi):
    mid = (lo + hi) // 2
    pivot = hi
    if arr[lo]<arr[mid]:
        if arr[mid]<arr[hi]:
            pivot = mid
    elif arr[lo]<arr[hi]:
        pivot = lo
    return pivot
def QuickSort( A, low, high ): 
    if low < high: 
        pivot = Partition( A, low, high) 
        QuickSort( A, low, pivot - 1 ) 
        QuickSort( A, pivot + 1, high) 

def Partition( A, low, high ) : 
    pivot = get_pivot(A, low, high)
    swap(A, pivot, high) 
    for i in range(low, high): 
        if A[i] <= A[high]: 
            swap( A, i, low)
            low += 1
    swap(A, low, high) 
    return low

def swap(arr: list, x: int , y: int):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

QuickSort(random_data, 0, len(random_data)-1)
print(random_data)