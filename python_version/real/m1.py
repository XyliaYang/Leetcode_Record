
if __name__ == "__main__":
    str_in=input()
    [n,a,b]=[int(n) for n in str_in.split(' ')]

    str_a=input()
    a_arr=[int(n) for n in str_a.split(' ')]

    str_b = input()
    b_arr = [int(n) for n in str_b.split(' ')]

    common_n=0
    for tmp in a_arr:
        if tmp  in b_arr:
            common_n+=1

    a_only=a-common_n
    b_only=b-common_n

    print(' '.join(str(i) for i in [a_only,b_only,common_n]))


