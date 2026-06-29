class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        used=[False]*len(nums)
        subset=[]
        self.solve(ans,subset,nums,used)
        return ans
    def solve(self,ans,subset,nums,used):
        if len(subset)==len(nums):
            ans.append(subset[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                continue
            subset.append(nums[i])
            used[i]=True
            self.solve(ans,subset,nums,used)
            subset.pop()
            used[i]=False



            