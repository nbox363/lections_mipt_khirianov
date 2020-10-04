""" Массив логических значений простоты числа
"""
N = 100
A =[True]*N
A[0] = A[1] = False

for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False

for k in range(N):
    print(k, '-', 'простое' if True else 'составное')