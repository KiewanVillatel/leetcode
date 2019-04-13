# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Time complexity : O(n)
# Space complexity: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        subStr = ["" for _ in range(numRows)]
        row = 0
        offset = -1 if numRows > 1 else 0
        # parcours each character
        for c in s:
            # assign character to its row
            subStr[row] += c
            # if we reach an extremity, go the other way
            if row == numRows - 1 or row == 0:
                offset *= -1
            row += offset

        # gather all rows
        return ''.join(subStr)


assert (Solution().convert("PAYPALISHIRING", 1) == "PAYPALISHIRING")
assert (Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
assert (Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
assert (Solution().convert("", 3) == "")
assert (Solution().convert("PAYPALISHIRING", 100) == "PAYPALISHIRING")
