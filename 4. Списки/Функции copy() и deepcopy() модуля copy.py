import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

spam2 = [[1, 2], [3, 4]]
cheese2 = copy.deepcopy(spam2)
cheese2[1] = 42
print(spam2)
print(cheese2)