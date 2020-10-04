""" Копирование массива
"""
N = int(input()) # размер массива
A = [0]*N
B = [0]*N
for k in range(N):
    A[k] = int(input())

for k in range(N):
    B[k] = A[k]

for k in range(N): # копирование задом-наперед
    B[k] = A[N-1-k]

C = list(A) # или так

V = [] # или так
V[:] = A
