def pipe_safe(*fns):
    def safe(x):
        try:
            for fn in fns:
                x = fn(x)
            return {"ok":True, "value":x}
        except Exception as e:
            return {"ok":False, "error":str(e)}
    return safe

# Тест
f = pipe_safe(lambda x:x+2, lambda x:x/0, lambda x:x*3)
print(f(5))  # → {"ok":False,"error":"division by zero"}

g = pipe_safe(lambda x:x+2, lambda x:x*3)
print(g(5))  # → {"ok":True,"value":21}
