"""Вывести список в виде строки значений разделенных запятыми.
    Последний элемент должен содержать слово end перед значением"""

spam = ['apples', 'bananes', 'tofu', 'cats']

def myDef(spam):
    spam[-1] = 'and ' + spam[-1]
    for i in spam:
            print(i + ', ', end = '')

myDef(spam)
