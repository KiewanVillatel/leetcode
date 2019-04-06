# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class Solution:

    def _findBestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def _getLongestString(self, p1, p2):
        return p1 if len(p1) > len(p2) else p2

    def longestPalindrome(self, s: str) -> str:
        best_palindrome = s[0] if len(s) else ""
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                left = i
                rigth = i + 1
                palindrome = self._findBestPalindrome(s, left, rigth)
                best_palindrome = self._getLongestString(palindrome, best_palindrome)
            if 0 < i < len(s) - 1:
                palindrome = self._findBestPalindrome(s, i - 1, i + 1)
                best_palindrome = self._getLongestString(palindrome, best_palindrome)
        return best_palindrome


print(Solution().longestPalindrome("absdsfaabaav"))
