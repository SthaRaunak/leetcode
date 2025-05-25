"""
    Problem: LeetCode 1 - Group Anagrams 

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    Possible Solution :

    1) Use sorted string as key 
    
    we iterate through each string in the array, 

    since anagrams produce same sorted string we sort each string and use sorted version as the key in a hashmap and group all the original strings that produce the same sorted string under that key.

    After processing all strings, we return the grouped lists (the values of the hashmap) as the final result.

    TC : O(m*nlogn)  [can change depending upon sorting algo used] 
    SC : O(m∗n)  

    2) Use list/array as key 

    We iterate through each string and initialize an array of size 26 (to represent each lowercase alphabet letter) with zeros.

    For each character in the string, we increment the value at the corresponding index in the array based on its position in the alphabet. This array effectively represents the frequency of each character in the string

    Since anagrams have the same character counts, this frequency array will be the same for all strings that are anagrams of each other. We use a tuple version of this array as the key in a hashmap (dictionary), grouping all strings with the same character frequency.

    After processing all strings, we return the grouped lists (the values of the hashmap) as the final result.

    TC: O(m*n) 
    SC: O(m*n)

    where m is the no of strings and n being the length of the longest string
"""


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res   = defaultdict(list)
        for s in strs:
            char_freq = [0] * 26
            for c in s:
                char_freq[ord(c) - ord('a')] += 1
            res[tuple(char_freq)].append(s)
        return list(res.values())
