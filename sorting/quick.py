import random 
random_data = [random.randint(1, i+1) for i in range(1024*12)]
data = [8, -1, 1, -3, 7, 0]
def QuickSort( A, low, high ): 
    if low < high: 
        pivot = Partition( A, low, high) 
        QuickSort( A, low, pivot - 1 ) 
        QuickSort( A, pivot + 1, high) 
def Partition( A, low, high ) : 
    pivot = low 
    swap( A, pivot, high) 
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

QuickSort(data, 0, len(data)-1)
print(data)