def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None

# Тест
print(find_first_even([1,3,5,6,7]))  # → 6
print(find_first_even([1,3,5]))      # → None
