"""def f(x):
    print(f'calculating {x}*10')
    return x * 10

a = (1, 2, 3, 4, 5)

b = (f(x) for x in a)

for y in b:
    print(y)"""

# ____________________________________________________________

"""def double_performer(f, x):
    return f(f(x))

def f(x):
    return x * 10

def f2(x):
    return x * x

def f3(x):
    return -x
f1 = f

for f in f, f2, f3:
    y = double_performer(f, 5)
    print(y)

A = (1, 2, 3, 4, 5)

C = map(f, A)

type(C)
print(C)

for y in C:
    print(y)"""

# ____________________________________________________________

"""A = range(10)
print(type(A))
B = (x for x in A if x % 2 == 0)
print(*(x * x for x in A if x % 2 ==1))"""

# ____________________________________________________________

A = (1, 2, 3, 4, 5)

B = tuple(x * 10 for x in A)

print(A)
print(B)
C = zip(A, B)
print(type(C))
C = zip(A, B)
for t in C:
    print(t[0] + t[1])

enumerate("HELLO")
for i, char in enumerate("HELLO"):
    print(i, char)

print(*map(lambda a: a[0] * a[1], *enumerate("HELLO")))

