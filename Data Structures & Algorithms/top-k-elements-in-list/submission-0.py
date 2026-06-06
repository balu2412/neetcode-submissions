class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        res=[]
        for i,j in d.items():
            res.append([j,i])
        res.sort()

        arr=[]
        while len(arr)<k:
            arr.append(res.pop()[1])
        return arr