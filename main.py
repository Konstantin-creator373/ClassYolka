size = int(input("Выберите размер треугольника: "))


def generation():
    n = size
    b = 0
    c = size + 1
    d = size * 2 + 2
    print(' ' * c, '**')
    for i in range(size):
        print(' ' * n, '*', " " * b * 2, '*')
        n -= 1
        b += 1
    print(' ', '*' * d)

def generation_fm():
    n = size
    b = 0
    c = size + 1
    d = size * 2 + 2
    x = b // 2
    print(' ' * c, '**')
    for i in range(size):
        if i == 7:
            print(' ' * n, '*', " " * b,"СНГ ФМ", '*')
            n -= 1
            b += 1
        else:
            print(' ' * n, '*', " " * b * 2, '*')
            n -= 1
            b += 1

    print(' ', '*' * d)

def sqare():
    w = size // 2
    v = size + size // 3
    for i in range(size // 2):
        print(' ' * w, '*' * v)

generation()
generation_fm()
generation()
sqare()








