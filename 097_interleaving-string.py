#!/usr/bin/env python
# -*- coding: utf8 -*-
import pytest


class Solution:
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        """DFS+记忆优化

        递归树参考：https://leetcode-cn.com/problems/interleaving-string/solution/shou-hua-tu-
jie-dfshui-su-dfsji-yi-hua-by-hyj8/
        """
        # 初始化，全部为空时匹配结束
        memo = {('', '', ''): True}

        def dfs(s1, s2, s3):
            key, flag = (s1, s2, s3), False
            # 已经记录匹配结果，则直接返回
            if key in memo:
                return memo.get(key)

            if s1 and s3 and s1[0] == s3[0] and dfs(s1[1:], s2, s3[1:]):
                flag = True
            if s2 and s3 and s2[0] == s3[0] and dfs(s1, s2[1:], s3[1:]):
                flag = True

            memo[key] = flag
            return flag

        return dfs(s1, s2, s3)

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        """类似路径问题，使用DP

        1.定义:dp[i][j]为s1前i个字符和s2[j]前j个字符是否能组成s3前i+j个字符
        2.递推公式：
            dp[i][j] = dp[i-1][j]&&s1[i-1]==s3[i+j-1] | dp[i][j-1]&&s2[j-1]==s3[i+j-1]

        参考：https://leetcode-cn.com/problems/interleaving-string/solution/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/
        """
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False
        if not s1 or not s2:
            return s1 == s3 or s2 == s3

        # 补位0
        dp = [[False for y in range(len2 + 1)] for x in range(len1 + 1)]
        dp[0][0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                        or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = True

        return dp[-1][-1]


@pytest.mark.parametrize(
    ('param1', 'param2', 'param3', 'res'),
    [('aabcc', 'dbbca', 'aadbbcbcac', True),
     ('aabcc', 'dbbca', 'aadbbbaccc', False),
     ('ab', 'cd', 'abcd', True),
     ('ab', 'ad', 'abad', True),
     ('db', 'b', 'cbb', False),
     ('a', 'b', 'a', False),
     ('', 'b', 'b', True),
     ('', '', 'a', False),
     ('', '', '', True),
     # 容易超时用例
     ('bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa',
      'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab',
      'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab', False)])
def test1(param1, param2, param3, res):
    solution = Solution()
    assert solution.isInterleave1(param1, param2, param3) == res
