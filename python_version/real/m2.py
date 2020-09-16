# @Time : 2020/9/6 10:15
# @Author : Xylia_Yang
# @Description :

if __name__ == '__main__':
    str=input()

    up_num=0
    lower_num=0

    for ch in str:
        if ch>='a' and ch<='z':
            lower_num+=1
        if ch>'A' and ch<='Z':
            up_num+=1

    half_num=int(len(str)/2)

    print(abs(half_num-lower_num))

