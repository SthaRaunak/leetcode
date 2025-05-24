"""
    Problem: LeetCode 1 - Two Sum 

    To find index of two numbers in array such that their sum is equals to target
    with assumption that every input has exactly one pair of indices i and j that satisfy the condition.

    
    Possible Solutions:

    1) Brute force
    
    check every combination of two values and check if sum is equal to target i.e we use two loops check sum of each element with every other until it results in target and then return the two indexes

    
    TC : O(n^2) 
    SC : O(1)

    2) Reaaranging the eqaution and using Hashmap (One pass)

    We rearrange equation as

    diff = target - nums[i]

    check if that diff exist in hashmap 
    if it exist in hashmap we just return the indexes as [hashmap[diff],i] 
    if not we put that diff in hashmap as key and its index as value 
    we perform this for each element in the array 

    This is clever as this way we are sure that indexes are different as hashmap only stores the values before index "i" and also hashmap[diff] < i

    We could also do it in two pass first put all element in the hashmap using first loop then in second loop do the check but we will have to check if index arent same as i != j

    TC : O(n) 
    SC : O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            hash_map = {} # map value to index 

            for i,n in enumerate(nums):
                diff = target - nums[i]
                if  diff in hash_map:
                    return [hash_map.get(diff),i]
                else:
                    hash_map[n] = i 

