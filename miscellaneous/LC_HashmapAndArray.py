from collections import Counter

def frequencySort(nums):
    freq = Counter(nums)
    freq_value_tuple = [(freq[num], -num) for num in nums]
    freq_value_tuple.sort()
    sorted_nums = [-pair[1] for pair in freq_value_tuple]

    return sorted_nums
# Examples
print(frequencySort([1, 1, 2, 2, 2, 3])) # Output: [3, 1, 1, 2, 2, 2]
