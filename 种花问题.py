'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
'''

class Solution(object):
    def canPlaceFlower(self, flowerbed, n):
        count = 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 2
            count += 1

        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[len(flowerbed)-1] = 2
            count += 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 2
                count += 1
        return True if count >= n else False
