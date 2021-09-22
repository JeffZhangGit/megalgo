# encoding=utf-8
# NC119 最小的K个数
# 思路，先排序，再取值
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k == 0:
            return []
        else:
            tinput.sort()
            return tinput[0:k]


s = Solution()
print s.GetLeastNumbers_Solution([1], 0)
print s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4)
print s.GetLeastNumbers_Solution([0, 1, 2, 1, 2], 3)
