class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1)%2!=0:
            l=0
            r=len(nums1)-1
            mid=(l+r)//2
            return float(nums1[mid])
        else:
            l=0
            r=len(nums1)-1
            mid=(l+r)//2
            res=(nums1[mid]+nums1[mid+1])/2
            return float(res)