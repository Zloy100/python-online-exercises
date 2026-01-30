def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}  # overrides перезаписывает

# Тест
defaults = {"x":1,"y":2}
overrides = {"y":10,"z":3}
print(merge_defaults(defaults, overrides))
# → {'x':1,'y':10,'z':3}
