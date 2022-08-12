import random
n = 100
random.seed(1)
data = [random.randint(0, x) for x in range(n)]

def bubble(arr):
    swapped = True
    for i in range(len(arr)):
        if not swapped:
            break
        for j in range(len(arr)-1, i, -1):
            if arr[j]<arr[j-1]:
                swap(arr, j, j-1)
                swapped = True

def swap(arr, x, y):
    z = arr[x]
    arr[x] = arr[y]
    arr[y] = z
# print(data)
bubble(data)
print(data)