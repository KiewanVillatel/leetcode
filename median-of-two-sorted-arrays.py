# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shortest_arr, longest_arr = (nums2, nums1) if len(nums1) > len(nums2) else (nums1, nums2)

        m = len(shortest_arr)
        M = len(longest_arr)

        half = (m + M) // 2

        left_size = half
        right_size = M + m - left_size

        i = (m + 1) // 2

        imin = 0
        imax = m

        if m == 0:
            return longest_arr[half] if M % 2 else (longest_arr[half - 1] + longest_arr[half]) / 2

        while True:
            j = half - i

            min_right, max_left = None, None

            if i == 0:
                max_left = longest_arr[j - 1]
            elif i == m:
                min_right = longest_arr[j]
            if j == 0:
                max_left = shortest_arr[i - 1]
            elif j == M:
                min_right = shortest_arr[i]

            if min_right is None:
                min_right = min(shortest_arr[i], longest_arr[j])
            if max_left is None:
                max_left = max(shortest_arr[i - 1], longest_arr[j - 1])

            if min_right >= max_left:
                if left_size == right_size:
                    return (max_left + min_right) / 2
                elif left_size > right_size:
                    return max_left
                else:
                    return min_right

            delta = max(1, (imax - imin) // 2)

            if max_left == shortest_arr[i - 1]:  # i too big
                imax = i
                i -= delta
            else:  # i too small
                imin = i
                i += delta


print(Solution().findMedianSortedArrays([1, 2, 3], [4, 5, 6]))
