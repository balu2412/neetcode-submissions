class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset=[]
        idx=0
        res=[]
        total=0
        self.solve(idx,subset,total,res,target,candidates)
        return res
    def solve(self,idx,subset,total,res,target,candidates):
        if total==target:
            res.append(subset[:])
            return
        if total>target:
            return
        if idx == len(candidates):
            return
        subset.append(candidates[idx])
        self.solve(idx,subset,total+candidates[idx],res,target,candidates)
        subset.pop()
        self.solve(idx+1,subset,total,res,target,candidates)