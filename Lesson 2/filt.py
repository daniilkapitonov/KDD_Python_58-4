def func(elem):
    return elem > 0
numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))
print(positive_numbers)
