def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Введите целове число: ')

try:
    intInput = int(input())
except:
    print('Введено не целове число, повторите ввод...')

while intInput != 1:
    intInput = collatz(intInput)
    print(intInput)


