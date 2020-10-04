''' Хеширование - преобразование массива входных данных произвольной длины 
                  в битовую строку фиксированной длины


    Хеш-функция - выполняет преобразование произвольных данных 
                  к данным фиксированной длины
        Свойства:
            1) Детерминированность - для одинаковых входных данных
                                     одинаковый выход
            2) Результат - фиксированная длина
            3) Лавинный эфект - когда немного меняются входные данные
                                результат меняется существенно
            4) Нет взаимнооднозначного соответствия между входными данными
               и ответом

        Ключевые свойства:
            1) Вычислительная сложность (быстро)
            2) Разрядность
            3) Криптостойскость 

        Свойства хорошей хеш-функции:
            1) Минимальное количество коллизий
            2) Равномерное распределение ответов
            3) Быстрое вычисление

        Идеальная хеш-функция - хеш-функция которая отображает каждый ключ из
                                набора 5 во множестве целых чисел без коллизий


    Хеш - результат


    Примеры хеш-функций:
        1) Остаток от деления
            H(X) = X mod N
            Пример:
                H(X) = x mod N
                H(X+N) mod N = H(X)
                |H(X) - H(X+1)| = 1  # осутствует лавинный эффект

        2) Полинимиальный кеш
            H(x) = ( Сигма(Xi) * k**i ) mod N

        3) XOR
            h = 0
            for c in X:
                h = h * c
        
        4) Цикличный добавочный ввод
            R(X) = P(X) * X**n mod G(X)
'''


def calc_hash(data):
    ''' Полинимиальный хеш'''
    k = 3571
    s = 0
    i = 1
    data += 84832941
    while data > 0:
        s += data % 2 * k**i
        i += 1
        data //= 2
    return s % 2 ** 8


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        if not self.search(element):
            node = [element, None]
            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node
            self.tail = node
    
    def search(self, element):
        curr = self.head
        while curr is not None:
            if curr[0] == element:
                return True
            curr = curr[1]
        return False


class HashTabl:
    def __init__(self):
        self.table = [LinkedList() for _ in range(256)]

    def add(self, element):
        hsh = calc_hash(element)
        self.table[hsh].add(element)

    def search(self, element):
        hsh = calc_hash(element)
        return self.table[hsh].search(element)
