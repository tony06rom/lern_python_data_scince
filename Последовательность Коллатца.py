def collatz(number):  # функция от значения
    if number % 2 == 0:   # если зачение является четным числом
        return number // 2   # напечатать значение деленное на 2
    elif number % 2 == 1:   # если зачение не является четным числом
        return 3 * number + 1   # напечатать значение умноженное на 3 и прибавить 1


try:
    print('Введите целове число: ')  # выводит на экран
    intInput = int(input())   # ввод числа
except:
    print('Введено не целове число, повторите ввод...')   # происходит отладка ошибки и выводит сообщение
    intInput = int(input())  # ввод числа

while intInput != 1:   # пока введенное число не будет равно 1
    intInput = collatz(intInput)   # введенное число будет подставляться в функцию collatz вместо number
    print(intInput)   # выводит фунцию collatz() с уже введенным значением в самом начале ( intInput = int(input()) )


