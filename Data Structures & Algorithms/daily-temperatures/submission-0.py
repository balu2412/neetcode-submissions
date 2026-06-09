class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n=len(t)
        res=[0]*n
        stack=[]
        
        for i in range(len(t)):
            while stack and t[i]>t[stack[-1]]:
                idx=stack.pop()
                res[idx]=i-idx

            stack.append(i)
        return res