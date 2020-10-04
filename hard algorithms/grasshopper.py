def traj_num(N):
    """ Сколько различных траекторий допргынуть из 1 в N?
        Прыгать можно на +1 и +2
    """
    K = [0,1] + [0]*N
    for i in range(2, N+1):
        K[i] = K[i-2] + K[i-1]
    return K[i]

traj_num(10)


def count_trajectories(N, allowed:list):
    """ Запретим некторые клетки для посещения (4,7)
        Прыгать можно на +1 и +2 +3
    """
    K = [0, 1, int(allowed[2])] + [0]*(N-3)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]

count_trajectories(10, [4,7])


def count_min_cost(N, price:list):
    """ Минимальная стоимость достижения клетки N
        price[i] - стоимость за посещение клетки i
        С[i] - минимальная стоимость достижения клетки i
        Прыгает на +1 и +2
        C(i) = price(i) + min(C(i-1),C(i-2))
    """
    C = [float('-inf'), price[1], price[1]+price[2]] + [0]*(N-2)
    for i in range(3, N+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[N]    