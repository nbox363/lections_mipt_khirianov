""" Генерация всех перестановок
    В первую позицию можно поставить любое из N чисел;
    Во вторую позицию можно поставить любое их N-1 чисел;
    (N)*(N-1)*(N-2)*...*(2)*(1) == N1
    Все числа от 000.0 до N-1.N-1 
"""

def generate_numbers(N:int, M:int, prefix=None): # N - основание системы счисления <= 10, M - длина числа, prefix - начинающиеся с
    """ Генерирует все числа
        Для произвольной системы счисления
    """

    prefix = prefix or []

    if M == 0:
        print(prefix)
        return
    
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

generate_numbers(3, 3)

####################################

def gen_bin(M, prefix=''):
    """ То же что, generate_numbers
        только без цикла for
        Только для двоичной системы счисления
    """
    if M == 0:
        print(prefix)
    else:
        gen_bin(M-1, prefix+'0')
        gen_bin(M-1, prefix+'1')

gen_bin(3)