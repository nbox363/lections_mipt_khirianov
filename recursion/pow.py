def pow(a, n):
    if n == 0:
        return 1
    else:
        return pow(a, n-1) * a

def pow_1(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1: # n - нечет
        return pow(a, n-1) * a
    else: # n - чет
        return pow(a**2, n//2)
        