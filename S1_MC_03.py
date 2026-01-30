def calc(a, op, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    match op:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _: return None

print(calc(10, "+", 5))
print(calc(10, "/", 0))
