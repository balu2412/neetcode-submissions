class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d=defaultdict(list)
        for i in range(9):
            res=[]
            for z in range(9):
                if board[i][z]!=".":
                    res.append(board[i][z])
            if len(res)!=len(set(res)):
                return False
            for j in range(9):
                if board[i][j]!=".":
                    d[j].append(board[i][j])
        for key,val in d.items():
            if len(val)!=len(set(val)):
                return False
        for r in range(0,9,3):
            for c in range(0,9,3):
                res=[]
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j]!=".":
                            res.append(board[i][j])
                if len(res)!=len(set(res)):
                    return False
        return True