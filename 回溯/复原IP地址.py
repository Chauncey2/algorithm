#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   复原IP地址.py
@Time    :   2023/03/31 15:34:16
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0）整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 
"192.168@1.1" 是 无效的 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
提示：

0 <= s.length <= 3000
s 仅由数字组成
#
"""

# here put the import lib




from typing import List
class Solution:
    def __init__(self) -> None:
        self.result = []

    def backtracking(self, s: str, start_index: int, point_num: int):
        # 终止条件
        if point_num >= 3:
            if self.is_valid(s, start_index,len(s)-1):
                self.result.append(s[:])
            return
        # 循环体
        for i in range(start_index, len(s)):
            if self.is_valid(s, start_index, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, point_num+1)
                # 回溯
                s = s[:i+1] + s[i+2:]
            else:
                break

    def restore_ip_addresses(self, s: str) -> List[str]:
        self.result.clear()
        # ip 只有四位，超过这个数量就不合法了
        if len(s) > 12: 
            return []
        self.backtracking(s,0,0)
        return self.result

    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False
        # 验证数字是否属于ip合法数字范围内
        if s[start] == "0" and start >= end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True

if __name__ == "__main__":
    s = "25525511135"
    print(Solution().restore_ip_addresses(s))
    