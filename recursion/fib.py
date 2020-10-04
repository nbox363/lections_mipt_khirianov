""" Динамическое программирование
"""


def fib(n):
    """ O(Fibo)
    """
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


n = 15
fibo = [0, 1] + [0]*(n-1)

for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[i])

print(f'число Фибоначи {n} = {fibo[i]}')


F = [None] * 10001
def fib(n):
    assert n >= 0 and n <= 10000
    if F[n] is not None:
        return F[n]
    elif n <= 1:
        F[n] = n
        return F[n]
    else:
        F[n] = fib(n-1) + fib(n-2)
        return F[n]
