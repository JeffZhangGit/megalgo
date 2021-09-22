# encoding=utf-8
# NC41 最长无重复子数组
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr):
        # write code here
        if not arr:
            return 0
        if len(arr) <= 1:
            return len(arr)
        else:
            maxlength = 0
            for i in range(len(arr)):
                result = []
                for j in range(i, len(arr)):
                    if arr[j] not in result:
                        result.append(arr[j])
                    else:
                        break
                if len(result) > maxlength:
                    maxlength = len(result)
            return maxlength


s = Solution()
print s.maxLength(None)
print s.maxLength([2, 3, 4, 5])
print s.maxLength([2, 2, 3, 4])
print s.maxLength([1])
print s.maxLength([1, 2, 3, 1, 2, 3, 2, 2])
print s.maxLength([2, 2, 3, 4, 8, 99, 3])
