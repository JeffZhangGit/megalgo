# encoding=utf-8
# NC141 判断回文
# 解法1： 𝑠𝑡𝑟[𝑖] != 𝑠𝑡𝑟[𝑙𝑒𝑛−1−𝑖]
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param str string字符串 待判断的字符串
# @return bool布尔型
#


class Solution:
    def judge(self, str):
        if str == None or len(str) == 1 or len(str) == 0:
            return True
        else:
            for i in range(len(str) / 2):
                if str[i] != str[-i - 1]:
                    return False
            return True


s = Solution()
print s.judge(None)
print s.judge('abc')
print s.judge('absba')
print s.judge('c')
print s.judge('1232131')
print s.judge('1111')
