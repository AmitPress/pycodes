ar = [-1, -8, 5, 0, -7, 9]
#     0   1   2  3   4  5

print(ar[0:5]) # right exclusive just like range -> [-1, -8, 5, 0, -7]
print(ar[0:]) # last element if not specified the right -> [-1, -8, 5, 0, -7, 9]
print(ar[1:]) # -> [-8, 5, 0, -7, 9]
print(ar[:]) # if not specified left is the leftmost and right is the rightmost -> [-1, -8, 5, 0, -7, 9]
print(ar[:3]) # -> [-1, -8, 5]

# does it support steps?
print(ar[:5:2]) # yes it does -> [-1, 5, -7]

# does it support inverse indexing?
print(ar[-1:1:-1]) # yes it does -> [9, -7, 0, 5]