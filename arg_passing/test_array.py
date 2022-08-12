arr1 = [45, 65, 32, 15]
arr2 = arr1
arr2[0] = 700
print(arr1)
arr3 = [65, 85, 30, 74, 100]
def junc(arr):
    arr[4] = 98
junc(arr3)
print(arr3)
# arrays are passed by value

ar1 = [98, 32, 74, 65]
ar2 = ar1.copy()
ar2[0] = 100
print(ar1, ar2)