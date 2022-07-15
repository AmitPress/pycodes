from email import message
from pyexpat.errors import messages


def ordinal_suffix(val):
    s = str(val)
    match s[-1]:
        case '11': return 'th'
        case '12': return 'th'
        case '13': return 'th'
        case '1': return 'st'
        case '2': return 'nd'
        case '3': return 'rd'
        case _: return 'th'

def ordinal(val):
    return str(val)+ordinal_suffix(val)

def nth_root(radicand, n):
    return radicand ** (1/n)

def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The"+ordinal(n)+" root of " \
        + str(radicand) + " is " + str(root)
    print(message)

display_nth_root(36, 2)