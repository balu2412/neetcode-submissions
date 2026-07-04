from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=dict()
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch]=set()
        
        indegree={}
        for ch in adj:
            indegree[ch]=0

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]

            minlen=min(len(w1),len(w2))

            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    parent = w1[j]
                    child = w2[j]
                    # Avoid duplicate edges
                    if child not in adj[parent]:
                        adj[parent].add(child)
                        indegree[child] += 1
                    break
            
        q=deque()
        for ch in indegree:
            if indegree[ch]==0:
                q.append(ch)
        res=[]
        while q:
            curr=q.popleft()
            res.append(curr)
                
            for i in adj[curr]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            
        if len(res)==len(adj):
            return "".join(res)
        return ""