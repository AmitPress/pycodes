def itr_fact(num):
    if num<0:
        return Exception('Negative number does not have factorial')
    result = 1
    while(num):
        result *= num
        num -= 1
    return result
print(itr_fact(9))