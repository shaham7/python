def checkIfExist(arr):
    seen = set()
    for num in arr:
        if 2 * num in seen or (num % 2 == 0 and num / 2 in seen):
            return True
        seen.add(num)
    return False

# Examples
print(checkIfExist([10, 2, 5, 3])) # Output: True
print(checkIfExist([3, 1, 7, 11])) # Output: False
