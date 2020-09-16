# @Time : 2020/9/6 10:27
# @Author : Xylia_Yang
# @Description :


if __name__ == '__main__':
    n=int(input())

    a_input=input()
    a_arr=[int(n) for n in a_input.split(' ')]

    res=0
    for i in range(n):
        tmp=a_arr[i]
        for j in range(n):
            tmp^=((i+1)%(j+1))
        res^=tmp

    print(res)

