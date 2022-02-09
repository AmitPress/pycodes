# def fun(arg):
#     return arg * 2
# print(fun(2))

# positional arguments
def parg(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)
# parg(p2=4, p1=5, p3=9) positional arguments can be made unordered

# default/optional argument
# def oparg(p1 = 45, p2, p3): # causes error because optional must follow postional
#     print(p1)
#     print(p2)
#     print(p3)

# oparg(25, 23, 9)

# def oparg(p2, p3, p1 = 45): # it works fine
#     print(p1)
#     print(p2)
#     print(p3)
# oparg(78, 12, p1 = 47)


# rule 001 : whether it is defining or calling a function,
                                                        # i)    positional arguments must precede optional
                                                        # ii)   all positional arguments must convert into optional to use them unorderly


