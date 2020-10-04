def count_sort(A):
    """ Сортировка подсчетом
        Q =[0]*10
    """
    Q = [0] * 10 # cортирую цифры
    for x in A:
        Q[x] += 1
    pos = 0 
    for x in range(0, 10): # (10, 0) по возрастанию
        for _i in range(Q[x]):
            A[pos] = x
            pos += 1
    return A

B = [1,2,4,5,1,2,8,9,0,1,2,4,5,6,1,2,3,9,0,7,6,8,9,1,4,5]

print(count_sort(B))
