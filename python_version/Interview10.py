# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 10:17
# @Author  : Xylia_Yang
# @Description ：

# 面试10题：Fibonacci数列
# 题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39
#  n=0时，f(n)=0 n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)

# 思路1：基于循环，时间复杂度为O（n）.从0计算到n
def  Fibonacci(n):
    if n<0:
        return  0
    if n<2:
        return n
    subOne=1
    subTwo=0

    for i in range(2,n+1):
        fibN=subOne+subTwo
        subTwo=subOne
        subOne=fibN
    return fibN

# 思路2：基于递归，效率低
def  FibonacciRecursion(n):
    if n<0:
        return 0
    if n<2:
        return n
    return FibonacciRecursion(n-1)+FibonacciRecursion(n-2)


# 题目拓展1：跳台阶
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
def stepStairs(n):
    if n<=0:
        return 0
    if n<=2:
        return n
    subOne=2
    subTwo=1
    for i in range(3,n+1):
        nStairs=subOne+subTwo
        subTwo=subOne
        subOne=nStairs
    return nStairs

if __name__=='__main__':
    print(Fibonacci(3))
    # print(FibonacciRecursion(3))







