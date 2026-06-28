class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        subset=[]
        idx=0
        total=0
        self.solve(idx,total,res,subset,candidates,target)
        return res
    def solve(self,idx,total,res,subset,candidates,target):
        if total==target:
            res.append(subset[:])
            return 
        if total>target:
            return
        if idx==len(candidates):
            return
        
        subset.append(candidates[idx])
        Sum=total+candidates[idx]
        self.solve(idx+1,Sum,res,subset,candidates,target)
        subset.pop()
        while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
            idx += 1
        self.solve(idx+1,total,res,subset,candidates,target)