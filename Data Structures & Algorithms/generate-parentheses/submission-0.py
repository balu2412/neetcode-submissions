class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        idx=0
        total=0
        brackets=[""]*(n*2)
        self.solve(idx,total,res,brackets)
        return res
    def solve(self,idx,total,res,brackets):
        if idx>=len(brackets):
            if total==0:
                res.append("".join(brackets))
            return 
        if total>len(brackets)//2:
            return 
        elif total<0:
            return 
        brackets[idx]="("
        sum=total+1
        self.solve(idx+1,sum,res,brackets)
        brackets[idx]=")"
        sum=total-1
        self.solve(idx+1,sum,res,brackets)