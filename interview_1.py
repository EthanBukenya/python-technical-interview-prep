# 1) Two Sum Problem – Efficient Python Solution
# Problem Statement
# You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target.

# Example
# nums = [2, 7, 11, 15]
# target = 9
# # Output: [0, 1] (Because 2 + 7 = 9)

# Optimized Approach – Hash Map
# Instead of using a brute-force approach with two loops, we can solve this problem efficiently using a hash map (dictionary).

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complementary = target - num
        if complementary in num_map:
            return [num_map[complementary], i]
        num_map[num] = i
    return []
# Why is this efficient?
# Time Complexity: O(n) – We iterate through the list once.
# Space Complexity: O(n) – Stores numbers and their indices in a dictionary.


if __name__ == '__main__':
    nums = [22, 34, 2, 10, 12, 1]
    target = 21
    print(two_sum(nums, target))
