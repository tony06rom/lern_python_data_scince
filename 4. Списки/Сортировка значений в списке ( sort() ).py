spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam2 = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam2.sort()
print(spam2)

spam.sort(reverse=True)
print(spam)

spam3 = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam3.sort()
print(spam3)

spam4 = ['a', 'z', 'A', 'Z']
spam4.sort(key=str.lower)
print(spam4)