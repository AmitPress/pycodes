# the compliment trick

# dry run for 8 and 1
def twosum(arr, target):
    m = {}
    for i, val in enumerate(arr):
        compliment = target - val # compliment = 9 - 8 = 1, for 1, compliment = 9 - 1 = 8
        if val in m.keys(): # 1 is in keys
            return [m[val], i] # m[1] == 2, i == 3
        else:
            m[compliment] = i # register m[1] = 2
    return [-1, -1]

print(twosum([2, 5, 8, 1, 2, 3], 4))