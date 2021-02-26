import math
def square():
    print('Введите сторону квадрата: ', end='')
    line = input()
    P = 4 * int(line)
    S = int(line) * int(line)
    D = math.sqrt(2) * int(line)
    print(tuple(P + S + D)
square()
