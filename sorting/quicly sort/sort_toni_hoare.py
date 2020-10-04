def hoare_sort(A): # Quick Sort
    if len(A) <= 1: # крайний случай
        return
    barier = A[0] # барьерный элемент
    L, R, M = [], [], [] 
    for x in A: # сравниваем барьерный элемент со всеми 
        if x < barier:
            L.append(x)
        elif x == barier:
            M.append(x)
        else: # x > barier
            R.append(x)
    hoare_sort(L)
    hoare_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1
    

B = [2, 4, 6, 1, 3, 4, 5]

hoare_sort(B)

print(*B)