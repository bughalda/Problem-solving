"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):

    def isPalindrome(self, x):
        x = str(x)
        left = 0
        right = len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        
        return True
