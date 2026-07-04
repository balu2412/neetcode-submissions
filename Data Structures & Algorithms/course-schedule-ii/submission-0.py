class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for u,v in prerequisites:
            adjlist[v].append(u)
            indegree[u]+=1
        queue=deque()
        res=[]

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            currentnode=queue.popleft()
            res.append(currentnode)

            for adjnode in adjlist[currentnode]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    queue.append(adjnode)
        
        if len(res)==numCourses:
            return res
        return []