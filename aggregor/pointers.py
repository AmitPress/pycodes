# two pointers to solve palindrome problem

from collections import defaultdict
def isPalindrome(string):
    i = 0
    j = len(string)-1
    while i<j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

# sttr = str(input())
# if isPalindrome(sttr):
#     print('palindrome')
# else:
#     print('not a palindrome')


# for two sum array must be sorted
def twosum(arr, target):
    mapping = defaultdict()
    for i, val in enumerate(arr):
        mapping[val]=i
    arr.sort()
    i = 0
    j = len(arr)-1

    while i<j:
        add = arr[i]+arr[j]
        if arr[i]+arr[j] == target:
            return mapping[arr[i]], mapping[arr[j]]
        elif add < target:
            i += 1
        else:
            j -= 1
    return -1, -1

li = list(map(int, input().split()))
target = int(input())

i, j = twosum(li, target)

print(f"{i} {j}")