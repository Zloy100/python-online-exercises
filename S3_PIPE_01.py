def pipe(*fns):
    def piped(x):
        for fn in fns:
            x = fn(x)
        return x
    return piped

# Тест
f = pipe(lambda x:x+2, lambda x:x*3, lambda x:x-1)
print(f(4))  # (4+2)*3-1 = 17
