#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   赎金信.py
@Time    :   2023/03/02 13:45:36
@Author  :   gaochangju 
@Version :   1.0
'''
"""
给定两个字符串（ransom ,magazine） 判断第一个字符串ransom ，能否由第二个字符串组成
要求，magazine中的每个字符只能用一次
可以认定 全部为小写字母
如果构成则返回 true，否则返回false
"""


def function(ransom: str, magazine: str) -> bool:
    # 要求时间复杂度和空间复杂度度都尽量最优，所以就不能直接使用map进行操作
    # 如果使用map对空间和时间的损耗都大，在时间上，map底层需要维护红黑树 ，做hash运算，费时

    if len(magazine) < len(ransom):
        return False

    letter = [0 for _ in range(26)]
    # 统计杂志中的每个小写字母出现的次数
    for m_c in magazine:
        letter[ord(m_c) - ord("a")] += 1
    for r_c in ransom:
        if letter[ord(r_c)-ord("a")] == 0:
            return False
        letter[ord(r_c)-ord("a")] -= 1
    return True


if __name__ == "__main__":
    ransom = "abcdh"
    magazine = "abcdefg"
    print(function(ransom, magazine))
