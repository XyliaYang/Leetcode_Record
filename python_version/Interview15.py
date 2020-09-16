# 题目： 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数

# 常规思路：用32次左移的1不断和该数字做与位运算，判断该位是否是1
def count_1(n):
    flag=1
    count=0

    for i in range(32):
        if n&flag:
            count+=1 #注意每一次，进行位运算，得到的结果还是位数，所以不能直接对输出结果累加
        flag=flag<<1
    return count


if __name__=='__main__':
    n=11
    print(count_1(n))


