def inspect(v):
    try:
        iterable = True
        iter(v)
    except:
        iterable = False

    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": iterable,
        "truthy": bool(v)
    }

values = [0, 1, "", "a", [], [1], {}, None, lambda x: x, 3.14]

for v in values:
    print(inspect(v))
