s1 = "a b c d"
s2 = s1
def same_mem(x,y):
    if id(x) == id(y):
        print("same memory")
    else:
        print("different memory")
same_mem(s1,s2)
arr1 = [4, 5]
arr2 = [5, 4]
arr3 = arr2
def foo(arry):
    same_mem(arr1, arry)
foo(arr1)
same_mem(arr1, arr2)
same_mem(arr2, arr3)
arr3 = arr2[:]
same_mem(arr2, arr3)