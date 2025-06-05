from bisect import bisect_left

class Solution:
    def maximumCount(self, nums):
        count_positive = len(nums) - bisect_left(nums, 1)
        count_negative = bisect_left(nums, 0)
        return max(count_positive, count_negative)