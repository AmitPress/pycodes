def bubble(A):
    swapped = True
    for i in range(len(A)):
        if not swapped:
            return
        for k in range(len(A) - 1, i, -1):
            if A[k] < A[k-1] :
                swap(A, k, k-1)
                swapped = True
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

A = [534,246,933, 127,277,32,454.565,220]
bubble(A)
print(A)