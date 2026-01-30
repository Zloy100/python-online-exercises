def invert(d):
    result = {}
    for k,v in d.items():
        if v in result:
            if isinstance(result[v], list):
                result[v].append(k)
            else:
                result[v] = [result[v], k]
        else:
            result[v] = k
    return result

# Тест
d = {"a":1,"b":2,"c":1}
print(invert(d))  # → {1:['a','c'], 2:'b'}
