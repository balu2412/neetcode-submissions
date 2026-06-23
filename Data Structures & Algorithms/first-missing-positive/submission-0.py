class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        
        j=1
        for i in range(0,len(nums)):
            if nums[i]>0 and nums[i]==j:
                j+=1
            elif nums[i]>0 and nums[i]!=j:
                return j
                exit()
        return j 