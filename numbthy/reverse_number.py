# def asis(n):
#     x = 0
#     i = 0
#     while(n):
#         rmd = n%10
#         n = n//10
#         if(i==0):
#             x = rmd
#         else:
#             x = rmd*10**i+x
#         i += 1
#     print(x)
# asis(98563215) # 98563215


def reversed(n):
    x = 0
    i = 0
    while(n):
        rmd = n%10
        n = n//10
        if(i==0):
            x = rmd
        else:
            x = x*10+rmd
        i += 1
    print(x)
reversed(987654321)