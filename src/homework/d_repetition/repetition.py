def get_factorial(num):
    result = 1
    for i in range(num + 1):
        if(i > 0):
            result *= i
    return result

def sum_odd_numbers(num):
    result = 0
    i = 0
    while i <= num:
        if((i % 2) == 1):
            result += i
        i += 1
    return result