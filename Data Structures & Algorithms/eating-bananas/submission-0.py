class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=[]
        min_p=1
        max_p=max(piles)
        while min_p<max_p:
            res.clear()
            a=(min_p+max_p)//2
            for i in range(len(piles)):
                if piles[i]%a==0:
                    res.append(piles[i]//a)
                else:
                    res.append((piles[i]//a)+1)
            if sum(res)>h:
                min_p=a+1
            else:
                max_p=a
        return min_p
