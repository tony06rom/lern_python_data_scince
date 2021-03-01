spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

print('_______________Ровняется___________________')

spam2 = {'name': 'Pooka', 'age': 5}
spam2.setdefault('color', 'black')
spam2.setdefault('color', 'white') # ни на чт оне повлияет, так как в ключе 'color' уже имеется значение
print(spam2)
