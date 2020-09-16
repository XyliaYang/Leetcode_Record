# @Time : 2020/4/13 9:29
# @Author : Xylia_Yang
# @Description :

# class Solution:
#     def reconstructQueue(self, people):
#

d={1:'c',2:'d',3:'b',4:'a'}


d.sort(key=lambda x:x[1])
print(d)

print(sorted(d.items(),key=lambda x:x[1]))