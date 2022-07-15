# 4 -- input
# 5
# 1 2 3 4 5
# 8
# 5 7 2 3 1 7 5 0
# 0
# 2
# 1 1
import sys
t = int(input())
while t:
    if int(input()):
        rm = list(map(int, sys.stdin.readline().split(' ')))
    else:
        t -= 1
        continue
    t -= 1
