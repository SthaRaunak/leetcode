
"""
    Problem: LeetCode 217 - Contains Duplicate
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    TC: O(n)
    SC: O(n)
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if(not(n in hash_set)):
                hash_set.add(n)
            else:
                return True

        return False 

