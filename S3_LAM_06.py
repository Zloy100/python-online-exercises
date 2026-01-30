def map_values(d, fn):
    return {k: fn(v) for k,v in d.items()}

d = {"a":1,"b":2,"c":3}
mapped = map_values(d, lambda x: x*10)
print(mapped)
# → {'a':10,'b':20,'c':30}
