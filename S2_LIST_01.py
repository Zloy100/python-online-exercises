def clean_numbers(values):
    out = []
    for v in values:
        try:
            out.append(float(v.strip()))
        except:
            pass
    return out

print(clean_numbers([" 1 ", "x", "2"]))
