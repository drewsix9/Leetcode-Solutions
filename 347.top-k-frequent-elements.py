#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)  # { num, count }
        for n in nums:
            count[n] += 1

        # Create a list of empty lists
        # index is the count of occurrences
        freq = [[] for _ in range(len(nums) + 1)]

        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(res) >= k:
                    break
                res.append(num)
        return res


# @lc code=end
