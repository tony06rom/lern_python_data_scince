

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Color': 'Mar 4'}

while True: # Пока правда - выполнять код
    print('Enter a name: (blank to quit)')
    name = input() # Ввод нового имени
    if name == '': # Если имя будет равно пустоте (два раза Enter)
        print('End program')
        break # выйти из цикла
    if name in birthdays: # Если имя уже содержится в словаре
        print(birthdays[name] + ' is the birthday of ' + name) # Напечатать значение имени в списке + текс + имя
    else: # Если ничего из перечисленного не выполняется
        print('I do not have birthday information of ' + name) # Напечатать текст + имя
        print('What is their birthday?')
        bday = input() # Ввод возраста для нового имени
        birthdays[name] = bday # Возраст вносится в словать с ключем введенного нового имени
        print('Birthday database update.')
