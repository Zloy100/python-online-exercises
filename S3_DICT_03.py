def pick(d, keys):
    return {k:d[k] for k in keys if k in d}

# Тест
d = {"a":1,"b":2,"c":3}
print(pick(d,["a","c","x"]))  # → {'a':1,'c':3}
