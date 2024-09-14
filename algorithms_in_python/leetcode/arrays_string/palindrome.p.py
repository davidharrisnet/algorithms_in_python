"""
Example 1: Given a string s, return true if it is a palindrome,
false otherwise.

A string is a palindrome if it reads the same forward as backward.
That means, after reversing it, it is still the same string.
For example: "abcdcba", or "racecar".
"""
def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
# This is the merge of merge_sort
def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans
"""
Example 4: 392. Is Subsequence.

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting 
some (or none) of the characters from the original string, while maintaining the relative 
order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)