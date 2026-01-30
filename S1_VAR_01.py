def fn(): pass

values = {
    "int": 1,
    "float": 1.5,
    "str": "hi",
    "bool": True,
    "none": None,
    "list": [1, 2],
    "tuple": (1, 2),
    "dict": {"a": 1},
    "set": {1, 2},
    "function": fn
}

for k, v in values.items():
    print(k, v, type(v), type(v).__name__)
