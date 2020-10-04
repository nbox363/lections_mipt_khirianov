import graphics as gr

window = gr.GraphWin("Russian game", 1000, 1000)
alpha = 0.1

def fractal(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B,C), (C,D), (D,A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)

    fractal(A1, B1, C1, D1, deep-1)

fractal((100,100), (100,500), (500,500), (100,500))

my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
my_rectangle.draw(window)
