def array_search(A:list, N:int, x:int): # A - массив, N - размер, x - искомое число
    """ Осуществялет поиск числа x в массиве A 
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента x в массиве A.
        Или -1, если такого нет.
        Если в массиве несколько элементов равных x,
        вернуть индекс первого по счету
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    print('#test1 - ok' if m == -1 else '#test1 - fail')

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    print('#test2 - ok' if m == 2 else '#test2 - fail')

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    print('#test3 - ok' if m == 0 else '#test3 - fail')

test_array_search()