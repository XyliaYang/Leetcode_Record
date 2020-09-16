# @Time : 2020/3/17 14:23
# @Author : Xylia_Yang
# @Description :


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices or len(prices)<2:
            return 0

        min=prices[0]
        max_diff=0

        for i in prices[1:]:
            cur_diff=i-min

            if cur_diff>max_diff:
                max_diff=cur_diff
            if i<min:
                min=i

        return max_diff


