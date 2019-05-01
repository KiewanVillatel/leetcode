# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def maxArea(self, heights) -> int:
        left_idx = 0
        right_idx = len(heights)-1

        max_container = 0

        while left_idx < right_idx:
            min_height = min(heights[left_idx], heights[right_idx])

            container = (right_idx - left_idx) * min_height

            max_container = max(container, max_container)

            if min_height == heights[left_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return max_container


assert (Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
assert (Solution().maxArea([1, 2]) == 1)
