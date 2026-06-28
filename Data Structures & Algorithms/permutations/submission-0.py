class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        self.solve(nums,res,path)
        return res
    def solve(self,nums,res,path):
        if len(path)==len(nums):
            res.append(path[:])
            return
        for num in nums:
            if num in path:
                continue
            path.append(num)
            self.solve(nums,res,path)
            path.pop()