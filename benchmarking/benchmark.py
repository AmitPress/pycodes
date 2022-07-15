def test():
    for i in range(10):
        for j in range(10):
            print(i,j)

import timeit
time_elapsed = timeit.Timer(test).timeit(number=5)
import os
os.system('clear')
print(time_elapsed)