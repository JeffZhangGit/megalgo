# encoding=utf-8
# NC95 数组中的最长连续子序列

#
# return the min number
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def minNumberdisappered(self, arr):
        if not arr or len(arr) == 0:
            return 1
        index = 1
        # arr = sorted
        if max(arr) < 0:
            return 1
        while index in arr:
            index = index + 1

        return index


s = Solution()
print s.minNumberdisappered([2, 3, 4, 5])
print s.minNumberdisappered([2, 2, 3, 4])
print s.minNumberdisappered([1, 1, 1, 1, 1])
