# encoding=utf-8
# NC127 最长公共子串

# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1 , str2 ):
        # write code here
        if not str1 or not str2:
            return ""
        else:
            pass
                


s = Solution()
print s.LCS([2, 3, 4, 5])
print s.LCS([2, 2, 3, 4])
print s.LCS([1])
