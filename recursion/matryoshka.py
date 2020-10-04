def matryoshka(n):
    if n == 1:
        print('Матрешечка')
    else:
        print('Верх матрешчки n =', n)
        matryoshka(n-1)
        print('Низ матрешчки n =', n)

matryoshka(5) 