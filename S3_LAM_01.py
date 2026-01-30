square = lambda n: n**2
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"

print(square(3), square(5), square(0))      # 9 25 0
print(is_odd(2), is_odd(3), is_odd(0))     # False True False
print(greet("Ola"), greet("Bob"), greet("")) # Hello, Ola! Hello, Bob! Hello, !
