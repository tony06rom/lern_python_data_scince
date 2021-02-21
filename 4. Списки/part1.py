['cat', 'bat', 'rat', 'elehpant']

[1, 2, 3]

['hello', 3.1415, True, None, 42]

spam = ['cat', 'bat', 'rat', 'elehpant']

print(spam)

print(spam[0])

print('Hello ' + spam[0])

spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(spam2[0])

print(spam2[1][1])

print(spam[-1])

print(spam[1:3])

print(len(spam))

spam[1] = 'aardvark'

print(spam)

Z = [1, 2, 3] + ['A', 'B', 'C']

print(Z)

spam3 = spam + Z

print(spam3)

del spam3[3]

print(spam3)

