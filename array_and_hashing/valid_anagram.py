"""
    Problem: LeetCode 242 - Valid Anagram 

    To determine if two strings are anagram of eachother

    Prereq:

    What is anagram?
    - An anagram is when we rearrange the characters of one string to form another string.

    Two possible solutions: 
    
    1) Sort the string then compare

    TC : O(s^2 + t^2) or O(slogs + tlogt)
    SC : O(1) or O(s+t) depending on sorting algorithm

    2) Use two hashmaps to store the frequencies of each character in the both the strings respectively and then compare the hashmap

    TC : O(s+t) 
    SC : O(1) as we have at most 26 char

    where s and t are length of strings being compared
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): # legnth should be equal for valid anagram
            return False 

        freqS,freqT = {},{}
            
        for i in range(len(s)):
            freqS[s[i]] = 1 + freqS.get(s[i],0)  #.get() in hashmap if key doesnt exist returns the second argument
            freqT[t[i]] = 1 + freqT.get(t[i],0) 

        if(freqS != freqT): 
            return False 
        
        return True 

