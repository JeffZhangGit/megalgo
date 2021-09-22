# encoding=utf-8
# NC103 反转字符串

# 反转字符串
# @param str string字符串
# @return string字符串
#
class Solution:
    def solve(self, str):
        if not str:
            return ""
        result = ""
        for i in range(len(str)):
            result = result + str[len(str) - 1 - i]
        return result


s = Solution()
print s.solve(None)
print s.solve('abc')
print s.solve('absba')
print s.solve('c')
print s.solve('1232131')
print s.solve('1111')
