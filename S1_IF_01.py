def shipping_cost(weight_kg, is_member):
    try:
        w = float(weight_kg)
    except:
        return None

    if w <= 0:
        return None
    if w <= 1:
        cost = 10
    elif w <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8

    return cost

tests = [0.5, 1, 5, 6, -1, "x"]

for t in tests:
    print(t, shipping_cost(t, True))
