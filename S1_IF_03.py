def normalize_name(x):
    if not x:
        return "Anonymous"
    x = x.strip()
    return x if x else "Anonymous"

tests = ["", " ", None, " Ola "]

for t in tests:
    print(t, "->", normalize_name(t))

