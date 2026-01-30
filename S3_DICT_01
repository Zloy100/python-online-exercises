def get_path(obj, path, fallback=None):
    keys = path.split(".")
    for k in keys:
        if not isinstance(obj, dict) or k not in obj:
            return fallback
        obj = obj[k]
    return obj

# Тест
d = {"a":{"b":{"c":42}}}
print(get_path(d,"a.b.c"))      # → 42
print(get_path(d,"a.b.x", -1))  # → -1
