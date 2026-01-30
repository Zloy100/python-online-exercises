lst = [1, 2, 3]
lst[0] = 99
print(lst)

tup = (1, 2, 3)
try:
    tup[0] = 99
except Exception as e:
    print(e)
