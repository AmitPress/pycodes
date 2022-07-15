import sys
def take_from_arg():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print(arg1, 'is okay')
    print(arg2, 'is not okay')
take_from_arg()