class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        res=[]
        idx=0
        subset=[]
        self.solve(idx,subset,res,arr,k)
        return res
    def solve(self,idx,subset,res,arr,k):
        if idx>=len(arr):
            if len(subset[:])==k:
                res.append(subset[:])
            return
        subset.append(arr[idx])
        self.solve(idx+1,subset,res,arr,k)
        subset.pop()
        self.solve(idx+1,subset,res,arr,k)