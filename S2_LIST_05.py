def stats(nums):
    if not nums:
        return None
    return {
        "min": min(nums),
        "max": max(nums),
        "sum": sum(nums),
        "avg": sum(nums)/len(nums)
    }

print(stats([1,-2,5,10]))
