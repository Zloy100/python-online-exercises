def grade(score):
    if not isinstance(score, (int, float)):
        return None
    if score < 0 or score > 100:
        return None
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

tests = [59, 60, 69, 70, 89, 90, 100, 101]

for t in tests:
    print(t, grade(t))
