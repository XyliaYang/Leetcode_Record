# @Time : 2020/3/12 10:23
# @Author : Xylia_Yang
# @Description :


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not str:
            return -1

        dict={}
        for cha in s:
            if not dict.get(cha):
                dict[cha]=1
            else:
                dict[cha]+=1

        index=0
        for key in dict.keys():
            if dict[key]==1:
                return index
            index+=1


if __name__=='__main__':
    str=""
    solution=Solution()
    print(solution.firstUniqChar(str))