# @Time : 2020/3/30 17:08
# @Author : Xylia_Yang
# @Description :

class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False

        rows=len(board)
        cols=len(board[0])

        visited=[[False]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.existCore(board,rows,cols,i,j,word,len(word),0,visited):
                    return True

        return False

    def existCore(self,board,rows,cols,i,j,word,length,index,visited):
        if index==length:
            return True

        if i<0 or  i>=rows or  j<0 or  j>=cols or visited[i][j] or index>=length:
            return False

        if board[i][j] != word[index]:
            return False

        visited[i][j]=True

        res=self.existCore(board,rows,cols,i-1,j,word,length,index+1,visited) \
            or self.existCore(board,rows,cols,i+1,j,word,length,index+1,visited) \
            or  self.existCore(board, rows, cols, i, j-1, word, length, index + 1, visited) \
            or self.existCore(board, rows, cols, i , j+1, word, length, index + 1, visited) \

        visited[i][j]=False
        return res


if __name__=='__main__':
    solution=Solution()
    board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word="ABCCED"
    print(solution.exist(board,word))