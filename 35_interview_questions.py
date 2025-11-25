# 1) Two Sum Problem – Efficient Python Solution
# Problem Statement
# You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target.

# Example
# nums = [2, 7, 11, 15]
# target = 9
# # Output: [0, 1] (Because 2 + 7 = 9)

# Optimized Approach – Hash Map
# Instead of using a brute-force approach with two loops, we can solve this problem efficiently using a hash map (dictionary).

# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complementary = target - num
#         if complementary in num_map:
#             return [num_map[complementary], i]
#         num_map[num] = i
#     return []
# # Why is this efficient?
# # Time Complexity: O(n) – We iterate through the list once.
# # Space Complexity: O(n) – Stores numbers and their indices in a dictionary.


# if __name__ == '__main__':
#     nums = [22, 34, 2, 10, 12, 1]
#     target = 21
#     print(two_sum(nums, target))


# 1. Debugging a Python Program
# python -m pdb script_name.py

# 2. yeild keyword
# def days(index):
#     day = ['S', 'M', 'T', 'W', 'Th', 'F', 'St']
#     yield day[index]
#     yield day[index+1]


# res = days(0)
# print(next(res), next(res))

# 3. Converting a List into a String or tuple or set

from collections import OrderedDict


def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length


if __name__ == '__main__':

    days = ['S', 'M', 'T', 'W', 'Th', 'F', 'St']
    # list_to_string = ' '.join(day)
    # list_to_string = str(day)
    list_to_tuple = tuple(days)
    list_to_set = set(days)

    # print(list_to_string)
    # print(list_to_tuple)
    # print(list_to_set)

    # print(days.count('M'))
    y = set(days)

    print([[x, days.count(x)] for x in y])
    print(y)

    print(length_of_longest_substring('abcdcdcbbc'))
