def has_duplicates(nums):

    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print(has_duplicates([1, 2, 3, 4, 1]))  # Output: True
print(has_duplicates([1, 2, 3, 4, 5]))  # Output: False

def has_duplicates(names):
    seen=set() 
    for name in names:
        if name in seen:
            return True
        seen.add(name)
    return False

print(has_duplicates(['Alice', 'Bob', 'Charlie', 'Alice']))  # Output: True
print(has_duplicates(['Alice', 'Bob', 'Charlie', 'David']))  # Output: False