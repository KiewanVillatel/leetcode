# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsInSubStr = {}
        i = 0
        j = 1
        if len(s):
            charsInSubStr[s[0]] = True
            bestLen = 1
        else:
            bestLen = 0
        while j < len(s):
            c2 = s[j]
            if c2 not in charsInSubStr:
                charsInSubStr[c2] = True
                if (j - i + 1) > bestLen:
                    bestLen = j - i + 1
                j += 1
            else:
                charsInSubStr.pop(s[i])
                i += 1
                if i == j:
                    charsInSubStr[s[j]] = True
                    j += 1
        return bestLen
