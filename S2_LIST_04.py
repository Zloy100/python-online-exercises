def flatten1(lst):
    out = []
    for x in lst:
        if isinstance(x, list):
            out.extend(x)
        else:
            out.append(x)
    return out

print(flatten1([1,[2,3],4,[5]]))
