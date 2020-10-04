def marge(A:list, B:list): 
    """ Слияние отсортированных массивов в один
    """
    C = [0] * (len(A) + len(B)) # создание списка соответсвующей длины
    i = k = n = 0 # три индекса для A, B и С соответственно 
    while i < len(A) and k < len(B): # пока один из массивов не закончится
        if A[i] <= B[k]: # сравниваем элементы списка A и B
            C[n] = A[i] # добавляем элемент A[i] в С
            i += 1
            n += 1
        else: # A[i] > B[k]
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A): # если первым закончился массив B
        C[n] = A[i] # переливаем все числа из А в С
        i += 1
        n += 1
    while k < len(B): # если первым закончился массив A
        C[n] = B[k] # переливаем все числа из B в С
        k +=1
        n += 1
    
    return C

def marge_sort(A): # будет делиться пока массив не будет состоять из одного элемента
    if len(A) <= 1: # проверка крайнего случая, когда список пустой или состоит из одного элемента
        return 
    middle = len(A)//2 # отмеряем половину массива
    L = [A[i] for i in range(0, middle)] # создаем левую половину 
    R = [A[i] for i in range(middle, len(A))] # создаем правую половину
    marge_sort(L) # рекурсия с ветвлением, быстро уходим к коротким спискам
    marge_sort(R)
    C = marge(L, R) # слить 
    for i in range(len(A)):
        A[i] = C[i]
     
B = [2, 4, 6, 1, 3, 4, 5]

marge_sort(B)

print(*B)