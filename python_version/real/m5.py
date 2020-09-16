# @Time : 2020/9/6 11:39
# @Author : Xylia_Yang
# @Description :


if __name__ == '__main__':
    n=int(input())

    q=[]
    while n>0:
        tmp=int(input())

        if tmp in q:
            q.remove(tmp)
        q.append(tmp)
        n-=1

    for i in range(len(q)):
        print(q.pop())

