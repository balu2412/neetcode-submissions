class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=0
        ans=[]
        board=["."*n for i in range(n)]
        left=[0]*n
        lower=[0]*(2*n-1)
        upper=[0]*(2*n-1)
        self.solve(col,ans,board,left,lower,upper,n)
        return ans
    def solve(self,col,ans,board,left,lower,upper,n):
        if n==col:
            ans.append(board[:])
            return

        for row in range(n):
            if ( left[row]==0 and 
                upper[n-1+col-row]==0 and 
                lower[row+col]==0 ):

                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                left[row]=1
                upper[n-1+col-row]=1
                lower[row+col]=1
                self.solve(col+1,ans,board,left,lower,upper,n)
                
                board[row]=board[row][:col]+"."+board[row][col+1:]
                left[row]=0
                upper[n-1+col-row]=0
                lower[row+col]=0