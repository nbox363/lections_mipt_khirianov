''' Хранение графа

Список вершин + список ребер
Требуется O(N) на перебор соседей вершины
'''

V0 = {'A', 'B', 'C', 'D'}  # множество вершин
E0 = {('A', 'B'), ('B', 'C'), ('C', 'D')}  # множество ребер



''' Матрица смежности '''

V3 = ['A', 'B', 'C', 'D']
index = {V3[i]: i for i in range(len(V3))}
A = [[0, 1, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [0, 0, 1, 0]]



''' Списки смежности '''

G = {'A': {'B'},
     'B': {'A', 'C'},
     'C': {'B', 'D'},
     'D': {'C'}
}

for neighbour in G['A']:  # перебор соседей
    print(neighbour)



''' Считывание с клавиатуры матрица смежности

N - количество вершин
M - количество ребер
'''

M, N = [int(i) for i in input().split()]

V = []

index = {}

A = [[0]*N for i in range(N)]

for i in range(N):
    v1, v2 = input().split()
    for v in v1, v2:
        if v not in index:
            V.append(v)
            index[v] = len(V)-1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1



''' Считывание с клавиатуры списки смежности '''

M, N = [int(i) for i in input().split()]

G = {}

for i in range(N):
    v1, v2 = input().split()
    for v, u in (v1, v2), (v2, v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)



''' Компактное хранение списков смежности
    для неизменяемого графа
'''

edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3]
offset = [0, 1, 4, 6, 9, 10]  # offset[i] - начало списка смежности i вершины
edges[offset[i]:offset[i+1]]