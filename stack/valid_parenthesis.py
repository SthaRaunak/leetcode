"""
    Problem: LeetCode 20 - Valid Parenthesis 
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    TC: O(n)
    SC: O(n)
"""



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")" : "(" , "]" : "[" , "}": "{"}
        
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False

        return not stack 

