from functools import reduce

nums = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2 == 0, nums))     # [2,4]
squares = list(map(lambda x: x**2, evens))           # [4,16]
total = reduce(lambda a,b: a+b, squares)             # 20
print(evens, squares, total)
