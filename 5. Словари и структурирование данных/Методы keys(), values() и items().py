spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
print('_______________________________________________')
for k in spam.keys():
    print(k)
print('_______________________________________________')
for i in spam.items():\
    print(i)
print('_______________________________________________')
print(spam.keys())
print('_______________________________________________')
print(list(spam.keys()))
print('_______________________________________________')
for h, t in spam.items():
    print('Key: ' + h + ' Value: ' + str(t))
