#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n

        pre = 1
        post = 1

        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res


# @lc code=end
