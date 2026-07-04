class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist=[[]  for _ in range (numCourses)]
        indegress=[0] * numCourses

        for u,v in prerequisites:
            adjlist[u].append(v)
            indegress[v]+=1
        
        q=deque()
        res=[]
        for i in range(numCourses):
            if indegress[i]==0:
                q.append(i)
        while q:
            currentnode=q.popleft()
            res.append(currentnode)
            for adjnode in adjlist[currentnode]:
                indegress[adjnode]-=1
                if indegress[adjnode]==0:
                    q.append(adjnode)
        
        if len(res)==numCourses:
            return True
        else:
            return False