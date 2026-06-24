class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s=0
        ans=float('inf')
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                s-=nums[l]
                ans=min(ans,i-l+1)
                l+=1
        if ans==float('inf'):
            return 0
        else:
            return ans