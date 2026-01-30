def compose(*fns):
    def composed(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return composed

# Тест
f = compose(lambda x:x+2, lambda x:x*3, lambda x:x-1)
print(f(4))  # ((4-1)*3)+2 = 11

# Проверка pipe vs compose с теми же функциями
p = pipe(lambda x:x+2, lambda x:x*3, lambda x:x-1)
c = compose(lambda x:x+2, lambda x:x*3, lambda x:x-1)
print(p(4), c(4))  # → 17 11
