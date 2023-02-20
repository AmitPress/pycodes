def fib(n:int)->int:
    if (n<=2): return 1
    return fib(n-2)+fib(n-1)

def hfib(n:int, memo:dict={})->int:
    if (n in memo): return memo[n]
    if (n<=2): return 1
    memo[n] = hfib(n-2, memo) + hfib(n-1, memo)
    return memo[n]

# print(fib(50)) # does not work
print(hfib(50))

