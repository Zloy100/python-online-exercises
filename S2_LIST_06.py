users = [
    {"id":1,"name":"ola","active":True},
    {"id":2,"name":"adam","active":False},
    {"id":3,"name":"eva","active":True},
]

res = sorted(
    [u["name"].upper() for u in users if u["active"]]
)

print(res)
