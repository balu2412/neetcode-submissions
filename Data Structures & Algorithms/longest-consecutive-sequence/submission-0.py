class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        b=sorted(nums)
        m=1
        count=1
        for i in range(1,len(nums)):
            if b[i]==b[i-1]:
                continue
            elif b[i]==b[i-1]+1:
                count+=1
                m=max(m,count)
            else:
                count=1
        return m