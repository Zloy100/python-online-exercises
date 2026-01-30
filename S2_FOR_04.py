def count_occurrences(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    return counts

# Тест
print(count_occurrences([1,2,2,3,1,1]))
# → {1:3, 2:2, 3:1}
