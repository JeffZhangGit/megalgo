# encoding=utf-8
# NC95 数组中的最长连续子序列

#
# max increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def MLS(self, arr):
        if not arr or len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1
        else:
            max_count = 0
            count = 1
            arr = sorted(arr)
            for i in range(1, len(arr)):
                if arr[i] - arr[i - 1] == 1:
                    count = count + 1
                else:
                    count = 1
                max_count = max(max_count, count)

            return max_count


s = Solution()
print s.MLS([2, 3, 4, 5])
print s.MLS([2, 2, 3, 4])
print s.MLS([1,1,1,1,1])
