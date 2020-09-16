
"""
思路1:python 数据大小及长度无限制
"""
def PrintToMaxOfDigits(n):
    num=10**n-1
    for i in range(num):
        print(i+1)




if __name__=='__main__':
    PrintToMaxOfDigits(2)

