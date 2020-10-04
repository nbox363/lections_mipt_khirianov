def chec_sorted(A, ascending=True): # ascending - восходящий
    """ Проверка отсортированности за O(N)
        N = len(A)
    """
    flag = True # предположительно отсортированный 
    s = 2*int(ascending)-1
    for i in range(0, len(A)-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag