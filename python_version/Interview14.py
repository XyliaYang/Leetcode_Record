# 题目：给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，2≤n≤58 并且 m≥2）。
# 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]k[1] … k[m] 可能的最大乘积是多少？
# 例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。

# 思路：贪婪算法。当n>=5时，尽可能剪成较多3的绳子；当n=4时，剪成两段2*2的

import math


def  maxProductCutRope(n):
    if n<2:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2

    numOf3=n/3
    if n-numOf3*3==1:
        numOf3-=1

    numOf2=(n-numOf3*3)/2
    return pow(3,numOf3)*pow(2,numOf2)


