#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for k in countS:
            if countS[k] != countT.get(k, 0):
                return False
        return True

        # @lc code=end
