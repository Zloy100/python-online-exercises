def parse_log(line):
    try:
        level, rest = line.split(":",1)
        parts = rest.strip().split()
        d = {"level":level}
        for p in parts:
            k,v = p.split("=")
            d[k] = v
        return d
    except:
        return None

lines = [
    "INFO: user=42 action=login",
    "ERROR: user=10 action=fail",
    "INFO: user=7 action=logout",
    "INFO: user=x action=login"
]

users = [int(d["user"]) for d in map(parse_log, lines) if d and d["level"]=="INFO" and d["user"].isdigit()]
print(users)  # → [42,7]
