# @Time : 2020/2/25 20:46
# @Author : Xylia_Yang
# @Description :

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return
        all_elements=[]
        d=0 #表示遍历的方向
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1

        while left<=right and top<=bottom:

            # 从左到右
            if d==0:
                for i in range(left,right+1):
                    all_elements.append(matrix[top][i])
                top+=1

            if d==1:
                for i in range(top,bottom+1):
                    all_elements.append(matrix[i][right])
                right-=1

            if d==2:
                for i in range(right,left-1,-1):
                    all_elements.append(matrix[bottom][i])
                bottom-=1

            if d==3:
                for i in range(bottom,top-1,-1):
                    all_elements.append(matrix[i][left])
                left+=1

            d=(d+1)%4

        return  all_elements







