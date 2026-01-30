import re

def normalize(s):
    s = s.strip()
    s = s.lower()
    s = re.sub(r'\s+', ' ', s)
    return s

# Тест
text = " Ala Ma Kota "
print(normalize(text))  # → "ala ma kota"
