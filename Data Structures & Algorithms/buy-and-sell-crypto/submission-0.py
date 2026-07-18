class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        minprice=nums[0]
        maxi=0
        for i in range(len(nums)):
            minprice=min(minprice,nums[i])
            for j in range(i,len(nums)):
                
                profit=nums[j]-minprice
                maxi=max(maxi,profit)
        return maxi