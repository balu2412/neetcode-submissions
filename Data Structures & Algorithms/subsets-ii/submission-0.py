class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset=[]
        res=[]
        idx=0
        self.solve(idx,subset,res,nums)
        return res
    def solve(self,idx,subset,res,nums):
        if idx>=len(nums):
            res.append(subset[:])
            return 
        subset.append(nums[idx])
        self.solve(idx+1,subset,res,nums)
        subset.pop()
        while idx+1<len(nums) and nums[idx]==nums[idx+1]:
            idx+=1
        self.solve(idx+1,subset,res,nums)