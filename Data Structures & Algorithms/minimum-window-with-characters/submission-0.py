class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s) and not t:
            return ""
        count=Counter(t)
        window={}
        have=0
        need=len(count)
        res=[-1,-1]
        reslen=float('inf')
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in count and window[c]==count[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=(r-l+1)
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if reslen!=float('inf'):
            return s[l:r+1]
        else:
            return ""