class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        res=""
        n,m=len(word1),len(word2)
        while i<n and j<m:
            res=res+word1[i]
            i+=1
            res=res+word2[j]
            j+=1
        if i<n:
            while i<n:
                res=res+word1[i]
                i+=1
        if j<m:
            while j<m:
                res=res+word2[j]
                j+=1
        return res