# data
import random
data = [5, -3, 0, -7, 5, 3, 1, 0, -9, 7]
random_data = [random.randint(1, i+1) for i in range(1024*12)]
def naive_bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j]<arr[j-1]:
                swap(arr, j, j-1)

def bubble_sort(arr: list):
    swapped = True
    for i in range(len(arr)):
        if not swapped:
            return
        for j in range(len(arr)-1, i, -1):
            if arr[j]<arr[j-1]:
                swap(arr, j, j-1)
                swapped = True

def swap(arr: list, x: int , y: int):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
def swap_val(x, y):
    temp = x
    x = y
    y = temp
def worst_sort(arr: list):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i]>arr[j]:
                swap_val(arr[i], arr[j])

def bubble(arr: list):
    for _ in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                swap_val(arr[j], arr[j+1])
# naive_bubble_sort(random_data)
# bubble_sort(random_data)
bubble(data)
print(data)
