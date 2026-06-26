class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=sorted(set(nums))
        nums[:len(a)]=a
        return len(a)