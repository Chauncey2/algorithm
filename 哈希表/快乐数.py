#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   快乐数.py
@Time    :   2023/03/01 22:11:42
@Author  :   gaochangju
@Version :   1.0
@Desc    :   None
'''

# 编写函数，判断一个数n是否为快乐数
# 快乐数：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def is_happy(nums:int)->int:
    
    def get_sum(n):
        s = 0
        while n:
           number = n %10
           s+= pow(number,2)
           n = n // 10
        return s
    
    res_set = set()
    # 不断对传入的数字进行计算
    while True:
        nums = get_sum(nums)
        print(nums)
        if nums == 1:
            return True
        if nums in res_set:
            return False
        else:
            res_set.add(nums)



if __name__ == "__main__":
    print(is_happy(19))