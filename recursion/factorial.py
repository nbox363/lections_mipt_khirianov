def f(n:int):
    # assert n >= 0, "Факториал отрицательного не определен"
    if n == 0:
        return
    return f(n-1) * n