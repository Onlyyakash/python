# def cube(x):
#     return x*x*x
# print(cube(5))  # Output: 125

# l = [1, 2, 4, 8, 10, 12]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# #     print(newl)

# newl = list(map(cube, l))
# print(newl)  # Output: [1, 8, 64, 512, 1000, 1728]

# def filter_function(a):
#     return a>8
# newnewl = list(filter(filter_function, l))
# print(newnewl)  # Output: [10, 12]

from functools import reduce
numbers = [1, 2, 3, 4, 5]
def mysum(x, y):
    return x + y
sum = reduce(mysum, numbers)
print(sum)  # Output: 15