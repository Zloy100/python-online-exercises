def unique(values):
    res = []
    for v in values:
        if v not in res:
            res.append(v)
    return res

print(unique([1,1,2,3,2,4]))
