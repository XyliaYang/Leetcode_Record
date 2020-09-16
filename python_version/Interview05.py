# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 9:46
# @Author  : Xylia_Yang
# @Description ：

# 面试5题：
# 题目：请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。

## 思路1：1.先计算出字符串中所含空格；2.用p2指针指向替换后字符串末尾，p1指向原字符串末尾；3.
## 从后向前遍历将p1所指字符复制到p2所指内容，如果遇到空格则用%20替换。时间复杂度为0(n).

def replace_(str):
    """
    python 字符串不能直接替换字符，需要转换成list之后完成替换再转换回来
    :param str:
    :return:
    """
    str_ls=list(str)
    p1=len(str_ls)-1

    blank_count=0
    for i in str_ls:
        if i==' ':
            blank_count+=1

    str_ls+=[None]*2*blank_count
    p2=len(str_ls)-1

    while p1!=p2 and p1>=0 and p2>=0:
        if  str_ls[p1]!=' ':
            str_ls[p2]=str_ls[p1]
            p1-=1
            p2-=1
        else:
            str_ls[p2]='0'
            p2-=1
            str_ls[p2]='2'
            p2-=1
            str_ls[p2]='%'
            p2-=1
            p1-=1
    return ''.join(str_ls)


## 思路2：python 内置字符串替换函数
def replace(str):
    return str.replace(' ','%20')

if __name__=='__main__':
    string=''
    print(replace_(string))



