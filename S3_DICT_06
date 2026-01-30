def group_by(items, key):
    result = {}
    for item in items:
        value = item.get(key)
        result.setdefault(value, []).append(item)
    return result

# Тест
users = [{"name":"Ola","age":20},{"name":"Bob","age":25},{"name":"Alice","age":20}]
print(group_by(users,"age"))
# → {20:[...],25:[...]}
