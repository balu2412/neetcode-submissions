class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        res=[]
        for num,fre in freq.items():
            res.append([fre,num])
        res.sort()

        arr=[]
        while len(arr)<k:
            arr.append(res.pop()[1])
        return arr