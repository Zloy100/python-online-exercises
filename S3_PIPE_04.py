def to_float_safe(strings):
    for s in strings:
        try:
            yield float(s.strip())
        except (ValueError, AttributeError):
            continue

# Тест
values = [" 1 ", "2.5", "x", " 3"]
total = sum(n*2 for n in to_float_safe(values))
print(total)  # (1*2)+(2.5*2)+(3*2) = 13.0
